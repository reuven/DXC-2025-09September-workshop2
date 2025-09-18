#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('filename')

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

if args.op == '+':
    result = args.first + args.second
elif args.op == '-':
    result = args.first - args.second
else:
    result = f'(Unknown operator {args.op})'

print(f'{args.first} {args.op} {args.second} = {result}')
