#!/usr/bin/python

import json

class DiscoverServices:

    def __init__(self, params):
        # TODO mejorar esto
        if type(params["hostname"]) is str:
            self.hostname = params["hostname"]
        if type(params["discover_services_mode"]) is str:
            self.mode = params["discover_services_mode"]


    def getRequest(self):
        ret = {}
        if hasattr(self, "hostname"):
            ret["hostname"] = self.hostname
        if hasattr(self, "mode"):
            ret["mode"] = self.mode


        return "request=" + json.dumps(ret)

    def getAdditionalURLParams(self):
        return ""
