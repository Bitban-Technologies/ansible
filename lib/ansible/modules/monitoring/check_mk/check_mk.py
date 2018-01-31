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
from ansible.modules.monitoring.check_mk.check_mk_fetch_url import FetchUrl
from ansible.modules.monitoring.check_mk.check_mk_add_host import AddHost
from ansible.modules.monitoring.check_mk.check_mk_activate_changes import ActivateChanges
from ansible.modules.monitoring.check_mk.check_mk_discover_services import DiscoverServices

def getArgumentSpec():
    return {
        "server": {"required": True, "type": "str"},
        "omdsite": {"required": True, "type": "str"},
        "action": {
            "required": True,
            #"choices": ["add_host", "edit_host", "delete_host", "get_host", "get_all_hosts", "discover_services", "activate_change"],
            "choices": ["add_host", "discover_services", "activate_changes"],
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
        "auto_activate_changes": {"default": False, "type": "bool"},
        "allow_foreign_changes": {"type": "int"},
        "auto_discover_services": {"default": False, "type": "bool"},
        "discover_services_mode": {"type": "str"},
    }

def actionsMapper(params):
    return {
        "add_host": AddHost(params),
        #"edit_host": "EditHost",
        #"delete_host": "DeleteHost",
        #"get_host": "GetHost",
        #"get_all_hosts": "GetAllHosts",
        "discover_services": DiscoverServices(params),
        "activate_changes": ActivateChanges(params),
    }


def main():

    module = AnsibleModule(
        argument_spec=getArgumentSpec()
    )

    actionClass = actionsMapper(module.params).get(module.params["action"])

    result = {}
    result["request"] = actionClass.getRequest()
    result["url"] = actionClass.getAdditionalURLParams()

    response, info = FetchUrl(module.params["server"],
                              module.params["omdsite"],
                              module.params["action"],
                              module.params["username"],
                              module.params["password"],
                              module,
                              actionClass.getRequest(),
    ).do()

    result["info"] = info

    try:
        result["response"] = json.loads(response.read())
    except Exception:
        result["response"] = {}
        module.fail_json(msg='Response can\'t read', **result)
    else:
        if result["response"]["result_code"] != 0:
            module.fail_json(msg=result["response"]["result"], **result)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
