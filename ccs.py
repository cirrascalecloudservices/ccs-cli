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
            if len(path)>0:
                params.append(('q', arr[0]))
            else:
                path.extend([a for a in arr[0].split('/') if a])
        else:
            params.append((arr[0], arr[1]))

    method = 'get'
    if len(path)>1:
        method='post'
    # url = '/'.join(['http://127.0.0.1:8080', *path])
    url = '/'.join(['https://api.cirrascale.net', *path])
    params.append(('_human', '1'))
    headers = {'Authorization': os.environ['CCS_KEY']}
    request = requests.Request(method, url, params=params, headers=headers).prepare()
    print(request.method, request.url, file=sys.stderr)
    response = requests.Session().send(request)
    print(response.text)
    sys.exit(0 if response.ok else 1)

if __name__ == "__main__":
    main()
