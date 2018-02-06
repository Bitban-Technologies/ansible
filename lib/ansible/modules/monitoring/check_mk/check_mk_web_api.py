import os, json, urllib
from ansible.module_utils.urls import fetch_url

class CheckMKWebApi:
    """
    Abstraction for Check_Mk Web API

    # Arguments
    check_mk_url (str): URL to Check_Mk web application, multiple formats are supported
    username (str): Name of user to connect as. Make sure this is an automation user.
    secret (str): Secret for automation user. This is different from the password!

    # Examples
    ```python
    WebApi('http://checkmk.company.com/monitor/check_mk/webapi.py', 'automation', 'secret')
    ```
    ```python
    WebApi('http://checkmk.company.com/monitor/check_mk', 'automation', 'secret')
    ```
    ```python
    WebApi('http://checkmk.company.com/monitor', 'automation', 'secret')
    ```
    """


    def __init__(self, check_mk_url, username, secret, module):
        check_mk_url = check_mk_url.rstrip('/')

        if check_mk_url.endswith('.py'):  # ends with /webapi.py
            self.web_api_base = check_mk_url
        elif check_mk_url.endswith('check_mk'):  # ends with /$SITE_NAME/check_mk
            self.web_api_base = os.path.join(check_mk_url, 'webapi.py')
        else:  # ends with /$SITE_NAME
            self.web_api_base = os.path.join(check_mk_url, 'check_mk', 'webapi.py')

        self.username = username
        self.secret = secret
        self.module = module

    def __build_request_data(self, data):
        if not data:
            return None
        return ('request=' + json.dumps(data)).encode()

    def __build_request_path(self, query_params=None):
        path = self.web_api_base + '?'

        if not query_params:
            query_params = {}

        query_params.update({
            '_username': self.username,
            '_secret': self.secret
        })

        query_string = urllib.urlencode(query_params)

        path += query_string
        return path


    def make_request(self, action, query_params=None, data=None):
        """
        Makes arbitrary request to Check_Mk Web API

        # Arguments
        action (str): Action request, e.g. add_host
        query_params (dict): dict of path parameters
        data (dict): dict that will be sent as request body

        # Raises
        CheckMkWebApiResponseException: Raised when the HTTP status code != 200
        CheckMkWebApiException: Raised when the action's result_code != 0
        """
        if not query_params:
            query_params = {}
        else:
            query_params = dict(query_params)  # work on copy

        query_params.update({'action': action})

        response, info = fetch_url(self.module,
                                   self.__build_request_path(query_params),
                                   data=self.__build_request_data(data),
                                   method="POST")

        if info["status"] != 200:
            raise Exception(info["msg"])

        try:
            return json.loads(response.read())
        except Exception:
            raise Exception("Response can't read")
