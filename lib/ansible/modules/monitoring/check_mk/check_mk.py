#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'Bitban'
}

DOCUMENTATION = '''
---
module: check_mk

short_description: Module for to manager check_mk

version_added: "2.4"

author:
    - César M. Cristóbal
'''

import json
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible.modules.monitoring.check_mk.check_mk_add_host import AddHost

def getArgumentSpec():
    return {
        "server": {"required": True, "type": "str"},
        "omdsite": {"required": True, "type": "str"},
        "action": {
            "required": True,
            #"choices": ["add_host", "edit_host", "delete_host", "get_host", "get_all_hosts", "discover_services", "activate_change"],
            "choices": ["add_host"],
            "type": "str"
        },
        "username": {"required": True, "type": "str"},
        # no_log is required to avoid the warning "warnings": ["Module did not set no_log for password"]
        "password": {"required": True, "type": "str", "no_log": True},
        "hostname": {"type": "str"},
        "attributes": {"type": "dict"},
        "unset_attributes": {"type": "list"},
        "folder": {"type": "str"},
        "sites": {"type": "list"},
        "autoActivateChange": {"default": False, "type": "bool"},
        "autoDiscoverServices": {"default": False, "type": "bool"},
    }

def actionsMapper(params):
    return {
        "add_host": AddHost(params),
        #"edit_host": "EditHost",
        #"delete_host": "DeleteHost",
        #"get_host": "GetHost",
        #"get_all_hosts": "GetAllHosts",
        #"discover_services": "DiscoverServices",
        #"activate_change": "ActivateChange",
    }


def main():

    module = AnsibleModule(
        argument_spec=getArgumentSpec()
    )

    actionClass = actionsMapper(module.params).get(module.params["action"])

    result = {}
    result["request"] = actionClass.getRequest()
    result["url"] = actionClass.getAdditionalURLParams()

    URL = "http://" + module.params["server"] + "/" + module.params["omdsite"] + "/check_mk/webapi.py"
    URL = URL + "?action=" + module.params["action"] + "&_username=" + module.params["username"] + "&_secret=" + module.params["password"]

    response, info = fetch_url(module,
                               URL,
                               data=actionClass.getRequest(),
                               method="POST")

    result["info"] = info

    try:
        result["response"] = response.read()
    except Exception:
        result["response"] = {}

    module.exit_json(**result)


if __name__ == '__main__':
    main()
