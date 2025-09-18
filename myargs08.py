#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('files', nargs='*', type=argparse.FileType('r'), required=True)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

for one_file in args.files:
    outfilename = one_file.name + '.output'  # Get output filename

    print(f'Reversing {one_file.name} into {outfilename}...')

    with one_file as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(one_line.rstrip()[::-1] + '\n')
