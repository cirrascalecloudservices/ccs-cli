#!/usr/bin/env python3

import os
import sys
import json
import time

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
  action = ''
  params = [] # http request params

  for arg in sys.argv[1:]:
    arr = arg.split('=', 1)
    if len(arr) == 1:
      if not action:
        action = arg # e.g., compute/install
      else:
        params.append(('q', arg)) # resources, e.g., gpuab12
    else:
      params.append((arr[0], arr[1])) # params, e.g., image=ubuntu/focal

  url = os.environ.get('CCS_URL') or 'https://api.cirrascale.net'
  ccs_key = os.environ.get('CCS_KEY') or open('/etc/ccs-key').read().splitlines()[0].split()[0]

  if ':' in action: # new style, e.g., always json, paging, work-queue, etc..
    method = 'get' if action.split(':')[1] == 'get' else 'post'
    next = requests.Request(method, f'{url}/{action}', params=params).prepare().url
    while next:
      request = requests.Request(method, next, headers={'Authorization': ccs_key}).prepare()
      print(request.method, request.url, file=sys.stderr) # debug
      response = requests.Session().send(request)
      next = response.json().get('next')
      if response.ok:
        for line in response.json().get('value', []):
          print(json.dumps(line), flush=True)
        time.sleep(int(response.headers.get('retry-after', '0'))) # honor retry-after seconds
      else:
        print(json.dumps(response.json()))
      method = 'get'
      # response.raise_for_status()
      if not response.ok:
        sys.exit(1)
  else: # old style
    if not action:
      action='get'
    if action!='get' and len(action.split('/'))<2:
      action = '/'.join([*action.split('/'), 'get'])
    method = 'get' if action.split('/')[-1] == 'get' else 'post'
    request = requests.Request(method, f'{url}/{action}', params=params if method=='get' else None, data=params if method=='post' else None, headers={'Authorization': ccs_key}).prepare()
    print(request.method, request.url, str(request.body or ''), file=sys.stderr) # debug
    response = requests.Session().send(request, stream=True)
    for line in response.iter_lines():
      print(line.decode(), flush=True)
    sys.exit(0 if response.ok else 1)

def ccsfmt():
  rows = []
  for line in sys.stdin:
    rows.append(json.loads(line))
  print(tabulate.tabulate(rows, headers='keys', tablefmt=tablefmt))

if __name__ == "__main__":
  ccs()
