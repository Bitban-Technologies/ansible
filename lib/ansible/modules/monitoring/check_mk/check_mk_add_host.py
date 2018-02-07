import re
from ansible.modules.monitoring.check_mk.check_mk_web_api import CheckMKWebApi
from ansible.modules.monitoring.check_mk.check_mk_params_helper import CheckMKParamsHelper

class AddHost:

    def __init__(self, module):
        self.api = CheckMKWebApi(module.params["check_mk_url"],
                                 module.params["username"],
                                 module.params["password"],
                                 module)


    def get_result(self, params):

        try:
            response = self.api.make_request("add_host", None, self.get_data(params))
        except Exception, message:
            return {"failed": True, "msg": message.message}

        if response["result_code"] == 0:
            response.update({"changed": True})
            return response
        if response["result_code"] == 1:

            regex = re.compile("Check_MK exception: Host .* already exists in the folder servers")

            if regex.match(response["result"]):
                response.update({"changed": False})
                return response


    def get_data(self, params):

        try:
            ret = CheckMKParamsHelper(params).get_mandatory_params(["hostname"])
        except Exception, message:
            raise Exception(message.message)

        ret.update(CheckMKParamsHelper(params).get_optional_params(["folder", "attributes", "create_folders"]))

        return ret