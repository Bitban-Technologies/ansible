from ansible.modules.monitoring.check_mk.check_mk_web_api import CheckMKWebApi
from ansible.modules.monitoring.check_mk.check_mk_params_helper import CheckMKParamsHelper

class DiscoverServices:

    def __init__(self, module):
        self.api = CheckMKWebApi(module.params["check_mk_url"],
                                 module.params["username"],
                                 module.params["password"],
                                 module)


    def get_result(self, params):

        try:
            response = self.api.make_request("discover_services", None, self.get_data(params))
        except Exception, message:
            return {"failed": True, "msg": message.message}

        if response["result_code"] == 1:
            response.update({"failed": True, "msg": response["result"]})

        response.update({"changed": True, "msg": response["result"]})

        return response


    def get_data(self, params):

        try:
            ret = CheckMKParamsHelper(params).get_mandatory_params(["hostname"])
        except Exception, message:
            raise Exception(message.message)

        ret.update(CheckMKParamsHelper(params).get_optional_params(["discover_services_mode"], {"discover_services_mode": "mode"}))

        return ret