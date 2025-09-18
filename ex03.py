#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments for name and company
parser.add_argument('first', type=float)
parser.add_argument('op')
parser.add_argument('second', type=float)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

# first, op, second = args.first, args.op, args.second

if args.op == '+':
    result = args.first + args.second
elif args.op == '-':
    result = args.first - args.second
else:
    result = f'(Unknown operator {args.op})'

print(f'{args.first} {args.op} {args.second} = {result}')
