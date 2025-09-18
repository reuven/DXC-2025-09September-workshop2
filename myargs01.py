#!/usr/bin/env python3

import sys

print(f'{len(sys.argv)=}')

for index, one_item in enumerate(sys.argv):
    print(f'{index}: {one_item}')
