# Ansible module for Check MK

## Development environment

Configure the environment:

```bash

$ virtualenv --python=/bin/python2.7 venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ . hacking/env-setup

```

How to test:

``` bash

$ ./venv/bin/python lib/ansible/modules/monitoring/check_mk/check_mk.py lib/ansible/modules/monitoring/check_mk/tests/args.json
$ ./bin/ansible-playbook lib/ansible/modules/monitoring/check_mk/tests/dev.yml

```

## How to install

pip2 install git+https://github.com/Bitban-Technologies/ansible.git@master


## Notes

The wato web api only returns as result code 0 if the request has been successful and result code 1 if not (http://git.mathias-kettner.de/git/?p=check_mk.git;a=blob;f=web/htdocs/webapi.py;h=e222c40b2113a46385f5bfb84fc3e200d2588bbe;hb=HEAD#l134)

Web API reference: http://mathias-kettner.com/cms_web_api_references.html
