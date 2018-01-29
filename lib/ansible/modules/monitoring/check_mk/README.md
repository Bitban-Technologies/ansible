# Ansible module for Check MK

## Development environment

$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ . hacking/env-setup

$ ./bin/ansible-playbook lib/ansible/modules/monitoring/check_mk/tests/dev.yml

## How to install

pip2 install git+https://github.com/Bitban-Technologies/ansible.git@master
