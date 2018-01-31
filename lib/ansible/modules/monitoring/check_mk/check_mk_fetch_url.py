#!/usr/bin/python

from ansible.module_utils.urls import fetch_url

class FetchUrl:

    def __init__(self, server, omdsite, action, username, password, module, requestData):
        self.server = server
        self.omdsite = omdsite
        self.action = action
        self.username = username
        self.password = password
        self.module = module
        self.requestData = requestData

    def do(self):

        URL = "http://" + self.server + "/" + self.omdsite + "/check_mk/webapi.py"
        URL = URL + "?action=" + self.action + "&_username=" + self.username + "&_secret=" + self.password

        return fetch_url(self.module,
                         URL,
                         data=self.requestData,
                         method="POST")
