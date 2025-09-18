#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments for name and company
parser.add_argument('-1', '--first', type=int)
parser.add_argument('-o', '--op')
parser.add_argument('-2', '--second', type=int)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

if args.op == '+':
    result = args.first + args.second
elif args.op == '-':
    result = args.first - args.second
else:
    result = f'(Unknown operator {args.op})'

print(f'{args.first} {args.op} {args.second} = {result}')
