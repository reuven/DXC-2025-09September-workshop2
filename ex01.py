#!/usr/bin/env python3

# # Exercise: Simple greeting

# 1. Write a command-line program that uses `sys.argv`.
# 2. It expects to get two arguments, a person's name and their company name.
# 3. It should print a greeting to the person using their company, too.

import sys

if len(sys.argv) != 3:
    print(f'You need to provide 2 arguments, a person name and a company name')

else:
    # tuple unpacking -- if sys.argv has 3 elements, it works great!
    program_name, person_name, company_name = sys.argv

    print(f'Hello, {person_name} from {company_name}!')
