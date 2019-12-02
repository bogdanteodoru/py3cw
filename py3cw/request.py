import hashlib
import hmac
import requests
import json
from .config import API_URL, API_VERSION, API_METHODS
from .utils import verify_request
from requests.exceptions import HTTPError


class Py3CW:

    def __init__(self, key: str, secret: str):
        """
        Init the library with a 3commas key and secret strings. Get keys from your account API
        (https://3commas.io/api_access_tokens) page
        """

        if key is None or key == '':
            raise ValueError('Please enter a 3commas API key')
        if secret is None or secret == '':
            raise ValueError('Please enter a 3commas API secret')

        self.key = key
        self.secret = secret

    def __generate_signature(self, path: str, data: str) -> str:
        """
        Generates the signature needed for 3commas API communication
        """
        encoded_key = str.encode(self.secret)
        message = str.encode(API_VERSION + path + data)
        signature = hmac.new(encoded_key, message, hashlib.sha256).hexdigest()
        return signature

    def __make_request(self, http_method: str, path: str, params: any, payload: any):
        """
        Private method that makes the actual request. Returns the response in JSON format for both
        success and error responses.
        """

        signature = self.__generate_signature(path, params)

        try:
            response = requests.request(
                method=http_method,
                url=API_URL + API_VERSION + path + '?' + params,
                headers={
                    'APIKEY': self.key,
                    'Signature': signature
                },
                data=payload
            )

            response_json = json.loads(response.text)

            if type(response_json) is dict and 'error' in response_json:
                return response_json, None
            else:
                return None, response_json

        except HTTPError as http_err:
            return {'error': True, 'msg': 'HTTP error occurred: {0}'.format(http_err)}, None

        except Exception as err:
            return {'error': True, 'msg': 'Other error occurred: {0}'.format(err)}, None

    @verify_request
    def request(self, entity: str, action: str = '', action_id: str = None, payload: any = None):
        """
        Constructs the API Url and makes the request.
        """

        api = API_METHODS[entity][action]
        method, api_path = api
        api_path = api_path.replace('{id}', action_id or '')

        return self.__make_request(
            http_method=method,
            path='{entity}{separator}{api_path}'.format(
                entity=entity,
                separator='/' if api_path else '',
                api_path=api_path or ''
            ),
            params='',
            payload=payload
        )
