#!/usr/bin/python

import json

class AddHost:

    def __init__(self, params):
        # TODO mejorar esto
        if type(params["attributes"]) is dict:
            self.attributes = params["attributes"]
        if type(params["folder"]) is str:
            self.folder = params["folder"]
        if type(params["hostname"]) is str:
            self.hostname = params["hostname"]


    def getRequest(self):
        ret = {}
        if hasattr(self, "attributes"):
            ret["attributes"] = self.attributes
        if hasattr(self, "folder"):
            ret["folder"] = self.folder
        if hasattr(self, "hostname"):
            ret["hostname"] = self.hostname

        return "request=" + json.dumps(ret)

    def getAdditionalURLParams(self):
        return ""
