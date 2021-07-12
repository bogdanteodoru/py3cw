import hashlib
import hmac
import requests
import json
from .config import API_URL, API_VERSION_V1, API_VERSION_V2, API_VERSION_V2_ENTITIES, API_METHODS
from .utils import verify_request
from requests.exceptions import HTTPError
from urllib.parse import urlencode, quote_plus
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class IPy3CW:
    def request(self, entity: str, action: str = '', action_id: str = None, payload: any = None):
        pass


class Py3CW(IPy3CW):

    def __init__(self, key: str, secret: str, request_options=None):
        """
        Init the library with a 3commas key and secret strings. Get keys from your account API
        (https://3commas.io/api_access_tokens) page
        """

        if request_options is None:
            request_options = {}
        if key is None or key == '':
            raise ValueError('Please enter a 3commas API key')
        if secret is None or secret == '':
            raise ValueError('Please enter a 3commas API secret')

        self.key = key
        self.secret = secret
        self.request_timeout = request_options.get('request_timeout', 30)
        self.request_retries_count = request_options.get('nr_of_retries', 5)
        self.request_retry_status_codes = request_options.get('retry_status_codes', [500, 502, 503, 504])

        """
        Set the number of retries to be 5 every 0.1 seconds... then 0.2, 0.3...
        You get the idea.
        """
        self.session = requests.Session()
        retries = Retry(
            total=self.request_retries_count,
            backoff_factor=0.1,
            status_forcelist=self.request_retry_status_codes
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def __generate_signature(self, path: str, data: str) -> str:
        """
        Generates the signature needed for 3commas API communication
        """
        encoded_key = str.encode(self.secret)
        message = str.encode(path + data)
        signature = hmac.new(encoded_key, message, hashlib.sha256).hexdigest()
        return signature

    def __make_request(self, http_method: str, path: str, params: any, payload: any, retry_count=0):
        """
        Private method that makes the actual request. Returns the response in JSON format for both
        success and error responses.
        """
        entity = path.split('/')[0]

        if entity in API_VERSION_V2_ENTITIES:
            path = path.replace('_v2', '')
            relative_url = f"{API_VERSION_V2}{path}"
        else:
            relative_url = f"{API_VERSION_V1}{path}"

        """
        If there are any params on the request, concatenate the strings together
        with the new params.
        """
        if params is not None and len(params) > 0:
            relative_url = relative_url + f"?{params}"

        """
        Make sure the payload is None if the method is GET or when in fact
        we have no payload.
        """
        if http_method == "GET" or (payload is not None and len(payload) == 0):
            payload = None

        signature = self.__generate_signature(relative_url, (json.dumps(payload) if payload is not None else ''))

        """
        Compute the absolute URL. Keep in mind that the signature generation for whatever reason doesn't
        work when you try to compute it with absolute URL. You need to create it with relative URL.
        """
        absolute_url = f"{API_URL}{relative_url}"

        try:
            response = self.session.request(
                method=http_method,
                url=absolute_url,
                headers={
                    'APIKEY': self.key,
                    'Signature': signature
                },
                json=payload,
                timeout=(self.request_timeout, self.request_timeout)
            )

            response_json = json.loads(response.text)

            if type(response_json) is dict and 'error' in response_json:
                error_status_code = response_json.get('error').get('status_code')
                if (
                    error_status_code and
                    error_status_code in self.request_retry_status_codes and
                    retry_count < self.request_retries_count
                ):
                    return self.__make_request(
                        http_method=http_method,
                        path=path,
                        params=params,
                        payload=payload,
                        retry_count=retry_count + 1
                    )
                else:
                    return response_json, {}
            else:
                return {}, response_json

        except HTTPError as http_err:
            return {'error': True, 'msg': 'HTTP error occurred: {0}'.format(http_err)}, None

        except Exception:
            return {'error': True, 'msg': 'Other error occurred: {} {} {}.'.format(
                response_json.get('error'),
                response_json.get('error_description'),
                response_json.get('error_attributes')
            )}, None

    @verify_request
    def request(self, entity: str, action: str = '', action_id: str = None, action_sub_id: str = None,
                payload: any = None):
        """
        Constructs the API Url and makes the request.
        """

        api = API_METHODS[entity][action]
        method, api_path = api
        api_path = api_path.replace('{id}', action_id or '')
        api_path = api_path.replace('{sub_id}', action_sub_id or '')
        is_get_with_payload = method == 'GET' and payload is not None

        return self.__make_request(
            http_method=method,
            path='{entity}{separator}{api_path}'.format(
                entity=entity,
                separator='/' if api_path else '',
                api_path=api_path or ''
            ),
            params=urlencode(payload, quote_via=quote_plus) if is_get_with_payload else '',
            payload=payload
        )
