#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser(description='Our wc version')

# add argument for filename
parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True,
                    help='Name of the file we want to count')

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

counts = {'lines':0,
          'words':0,
          'chars':0}

with args.file as f:
    for one_line in f:
        counts['lines'] += 1
        counts['chars'] += len(one_line)          # count characters in the line
        counts['words'] += len(one_line.split())  # break the line into words, and count them

# args.file.close()

for key, value in counts.items():
    print(f'{key}:{value}')
