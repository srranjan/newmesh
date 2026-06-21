#!/usr/bin/env python3

from ansible.module_utils.basic import AnsibleModule
import requests

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type='str', required=True),
            method=dict(type='str', default='POST'),
            body=dict(type='dict', default={})
        )
    )
    
    try:
        response = requests.post(
            module.params['url'],
            json=module.params['body']
        )
        
        result = {
            'changed': True,
            'status_code': response.status_code,
            'response': response.json()
        }
        
        module.exit_json(**result)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()

