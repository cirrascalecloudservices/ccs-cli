#!/usr/bin/env python3

import os
import sys
import json

import tabulate

tabulate.MIN_PADDING = 0

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


def main():
    rows = []
    for line in sys.stdin:
        rows.append(json.loads(line))
    print(tabulate.tabulate(rows, headers="keys", tablefmt=tablefmt))


if __name__ == "__main__":
    main()
