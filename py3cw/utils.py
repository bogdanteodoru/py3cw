from .config import API_METHODS


def verify_request(func):
    def wrapper(*args, **kw):
        """
        Raises an error if on of the arguments is missing or if the specific action requires and ID
        and it is not sent.
        """

        entity = kw.get('entity')
        action = kw.get('action')
        action_id = kw.get('action_id')
        api = API_METHODS[entity][action]
        method, api_path = api

        if entity is None or entity == '':
            raise ValueError('Missing entity')
        if entity not in API_METHODS:
            raise ValueError('Invalid entity')
        if action not in API_METHODS[entity]:
            raise ValueError('Invalid action')
        if '{id}' in api_path and (action_id is None or action_id == ''):
            raise ValueError('Missing ID for {action}'.format(action=action))

        return func(*args, **kw)

    return wrapper
