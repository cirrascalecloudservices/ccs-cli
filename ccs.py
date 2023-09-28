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

    # url = '/'.join(['http://127.0.0.1:8080', *args])
    url = '/'.join(['https://api.cirrascale.net', *args])
    params.append(('_format', 'text'))
    headers = {'Authorization': os.environ['CCS_KEY']}
    response = requests.post(url, params=params, headers=headers)
    print(response.text)
    sys.exit(0 if response.ok else 1)


if __name__ == "__main__":
    main()
