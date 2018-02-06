
import json
import re
from ansible.modules.monitoring.check_mk.check_mk_web_api import CheckMKWebApi

class AddHost:

    def __init__(self, module):
        self.api = CheckMKWebApi(module.params["check_mk_url"],
                                 module.params["username"],
                                 module.params["password"],
                                 module)


    def get_result(self):

        try:
            response = self.api.make_request("add_host")
        except Exception, message:
            return {"fail": True, "msg": message.message}

        print(response)