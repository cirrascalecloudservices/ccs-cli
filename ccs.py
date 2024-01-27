#!/usr/bin/env python3

import os
import requests
import sys

def main():
    path = []  # http path
    params = []  # http request params

    for arg in sys.argv[1:]:
        arr = arg.split('=', 1)
        if len(arr) == 1:
            if len(path)==0: # first unnamed is noun/verb
                path.extend([a for a in arr[0].split('/') if a])
            else:
                params.append(('q', arr[0]))
        else:
            params.append((arr[0], arr[1]))

    if len(path)<2:
        if path!=['get']:
            path.append('get')
    method = path[-1]
    if method!='get':
        method='post'
    # url = '/'.join(['http://127.0.0.1:8080', *path])
    url = '/'.join(['https://api.cirrascale.net', *path])
    ccs_key = os.environ.get('CCS_KEY')
    if not ccs_key:
        ccs_key = open('/etc/ccs-key').read().splitlines()[0].split()[0]
    headers = {'Authorization': ccs_key}
    request = requests.Request(method, url, params=params if method=='get' else None, data=params if method=='post' else None, headers=headers).prepare()
    print(request.method, request.url, request.body, file=sys.stderr)
    params.append(('_human', '1'))
    request = requests.Request(method, url, params=params if method=='get' else None, data=params if method=='post' else None, headers=headers).prepare()
    response = requests.Session().send(request)
    print(response.text.strip())
    sys.exit(0 if response.ok else 1)

if __name__ == "__main__":
    main()
