#!/usr/bin/env python3

import os
import requests
import sys

def main():
    path = []  # http path
    params = []  # http query params

    for arg in sys.argv[1:]:
        arr = arg.split('=', 1)
        if len(arr) == 1:
            if len(path)==0:
                path.extend([a for a in arr[0].split('/') if a])
            else:
                params.append(('q', arr[0]))
        else:
            params.append((arr[0], arr[1]))

    if len(path)<2:
        if path!=['get']:
            path.append('get')
    method = 'get'
    if path[-1]!='get':
        method='post'
    # url = '/'.join(['http://127.0.0.1:8080', *path])
    url = '/'.join(['https://api.cirrascale.net', *path])
    headers = {'Authorization': os.environ['CCS_KEY']}
    request = requests.Request(method, url, params=params, headers=headers).prepare()
    print(request.method, request.url, file=sys.stderr)
    params.append(('_human', '1'))
    request = requests.Request(method, url, params=params, headers=headers).prepare()
    response = requests.Session().send(request)
    print(response.text.strip())
    sys.exit(0 if response.ok else 1)

if __name__ == "__main__":
    main()
