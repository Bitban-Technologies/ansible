from ansible.modules.monitoring.check_mk.check_mk_web_api import CheckMKWebApi
from ansible.modules.monitoring.check_mk.check_mk_params_helper import CheckMKParamsHelper

class ActivateChanges:

    def __init__(self, module):
        self.api = CheckMKWebApi(module.params["check_mk_url"],
                                 module.params["username"],
                                 module.params["password"],
                                 module)


    def get_result(self, params):

        try:
            response = self.api.make_request("activate_changes", None, self.get_data(params))
        except Exception, message:
            return {"failed": True, "msg": message.message}

        if response["result_code"] == 1:
            response.update({"failed": True, "msg": response["result"]})

        return response


    def get_data(self, params):

        ret = {}

        sites = params.get("sites")
        if sites == None:
            raise Exception("sites is a mandatory field")

        ret.update({"sites": sites})
        ret.update(CheckMKParamsHelper(params).get_optional_params(["allow_foreign_changes"]))

        return ret