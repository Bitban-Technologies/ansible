#!/usr/bin/python

import json

class ActivateChanges:

    def __init__(self, params):
        # TODO mejorar esto
        if type(params["sites"]) is dict:
            self.sites = params["sites"]
        else:
            self.sites = [params["omdsite"]]
        if type(params["allow_foreign_changes"]) is int:
            self.allow_foreign_changes = params["allow_foreign_changes"]


    def getRequest(self):
        ret = {}
        if hasattr(self, "sites"):
            ret["sites"] = self.sites
        if hasattr(self, "allow_foreign_changes"):
            ret["allow_foreign_changes"] = self.allow_foreign_changes

        if ret == {}:
            return ""

        return "request=" + json.dumps(ret)

    def getAdditionalURLParams(self):
        return ""
