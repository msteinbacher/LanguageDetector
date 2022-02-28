import requests


class RESTClient:
    """
    responsible for JSON and RESTful clients
    """

    def __init__(self):
        self.input = None
        self.output = None
        self.is_reliable = None
        self.lang_short = None
        self.lang_long = None
        self.probability = None
        self.path = "http://127.0.0.1:5000/lg"

    def check_language(self, key: str):
        """
        checks the given input for language from REST Client
        :param self, key
        """
        self.input = key
        try:
            response = requests.get(self.path, params={'id': self.input}).json()
            if not 'error' in response:
                self.lang_long = response['language']
                self.lang_short = response['short']
                self.is_reliable = response['reliable']
                self.probability = response['prob']
            else:
                raise InvalidValueError

        except requests.exceptions.ConnectionError:
            raise InternetConnectionError


class InternetConnectionError(Exception):
    """Gets thrown when no internet connection available"""
    pass


class InvalidValueError(Exception):
    """Gets thrown when input is invalid"""
    pass
