#!/usr/bin/env python3

import os
import sys
import json

import requests
import tabulate

tabulate.MIN_PADDING=0

tablefmt = tabulate.TableFormat(
    lineabove=tabulate.Line("-", "-", "--", "-"),
    linebelowheader=tabulate.Line("-", "-", "--", "-"),
    linebetweenrows=None,
    linebelow=tabulate.Line("-", "-", "--", "-"),
    headerrow=tabulate.DataRow(" ", "  ", " "),
    datarow=tabulate.DataRow(" ", "  ", " "),
    padding=0,
    with_header_hide=None,
)

def ccs():
    path = []  # http path
    params = []  # http request params
    _format = 0

    for arg in sys.argv[1:]:
        arr = arg.split('=', 1)
        # named
        if len(arr) > 1:
            params.append((arr[0], arr[1]))
            if arr[0]=='_format':
                _format=int(arr[1])
        # unnamed
        else:
            if len(path)==0: # first unnamed is noun/verb
                path.extend(arr[0].split('/'))
            else:
                params.append(('q', arr[0]))

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
    request = requests.Request(method, url, params=params if method=='get' else None, data=params if method=='post' else None, headers={'Authorization': ccs_key}).prepare()
    print(request.method, request.url, str(request.body or ''), file=sys.stderr)
    response = requests.Session().send(request, stream=True)

    if _format:
        rows=[]
        for line in response.iter_lines():
            rows.append(json.loads(line))
        print(tabulate.tabulate(rows, headers='keys', tablefmt=tablefmt))
    else:
        for line in response.iter_lines():
            print(line.decode())

    sys.exit(0 if response.ok else 1)


def ccsfmt():
    rows = []
    for line in sys.stdin:
        rows.append(json.loads(line))
    print(tabulate.tabulate(rows, headers="keys", tablefmt=tablefmt))


if __name__ == "__main__":
    ccs()
