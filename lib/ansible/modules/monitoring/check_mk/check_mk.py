#!/usr/bin/python
# -*- coding: utf-8 -*-

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

from ansible.module_utils.basic import AnsibleModule
from ansible.modules.monitoring.check_mk.check_mk_add_host import AddHost
from ansible.modules.monitoring.check_mk.check_mk_activate_changes import ActivateChanges
from ansible.modules.monitoring.check_mk.check_mk_discover_services import DiscoverServices

def getArgumentSpec():
    return {
        "check_mk_url": {"required": True, "type": "str"},
        "action": {
            "required": True,
            #"choices": ["add_host", "edit_host", "delete_host", "get_host", "get_all_hosts", "discover_services", "activate_change"],
            "choices": ["add_host", "discover_services", "activate_changes"],
            "type": "str"
        },
        "username": {"required": True, "type": "str"},
        # no_log is required to avoid the warning "warnings": ["Module did not set no_log for password"]
        "password": {"required": True, "type": "str", "no_log": True},
        "hostname": {"type": "str", "default": None},
        "attributes": {"type": "dict", "default": None},
        "unset_attributes": {"type": "list", "default": None},
        "folder": {"type": "str", "default": None},
        "sites": {"type": "list", "default": None},
        "auto_activate_changes": {"type": "bool", "default": False},
        "allow_foreign_changes": {"type": "int", "default": 0},
        "auto_discover_services": {"type": "bool", "default": False},
        "discover_services_mode": {"type": "str", "default": None},
    }

def actionsMapper(module):
    return {
        "add_host": AddHost(module),
        #"edit_host": "EditHost",
        #"delete_host": "DeleteHost",
        #"get_host": "GetHost",
        #"get_all_hosts": "GetAllHosts",
        #"discover_services": DiscoverServices(module),
        #"activate_changes": ActivateChanges(module),
    }


def main():

    module = AnsibleModule(
        argument_spec=getArgumentSpec()
    )

    action = actionsMapper(module).get(module.params["action"])

    result = action.get_result()

    if result["fail"]:
        module.fail_json(**result)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
