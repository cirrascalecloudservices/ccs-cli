#!/usr/bin/env python3
import argparse
import os
import requests
import sys


def main():
    args = []  # http path args
    params = []  # http query params

    knowns, unknowns = argparse.ArgumentParser().parse_known_args()
    for unknown in unknowns:
        arg = unknown.split('=', 1)
        if len(arg) == 1:
            args.append(arg[0])
        else:
            params.append((arg[0], arg[1]))

    ccs = os.path.basename(sys.argv[0])
    api = '-'.join([*reversed(ccs.split('-')[1:]), 'api'])
    key = '_'.join([*ccs.split('-'), 'key']).upper() # e.g., CCS_KEY
    # url = '/'.join(['http://localhost:8080', *args])
    url = '/'.join(['https://{}.cirrascale.net'.format(api), *args])
    params.append(('_format', 'text'))
    headers = {'Authorization': os.environ[key]}
    response = requests.post(url, params=params, headers=headers)
    print(response.text)
    sys.exit(0 if response.ok else 1)


if __name__ == "__main__":
    main()
