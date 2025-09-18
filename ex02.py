#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments for name and company
parser.add_argument('name')
parser.add_argument('age')

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

print(args)

# grab the names via attributes on "args"
print(f'Hello, {args.name} from {args.age}!')
