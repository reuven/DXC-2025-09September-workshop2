#!/usr/bin/env python3

import cmd

class Calculator(cmd.Cmd):
    def do_add(self, line):
        numbers = [int(one_number)
                   for one_number in line.split()]
        print(f'add, {line=}, {numbers=}')

    def do_sub(self, line):
        print(f'sub, {line=}')

    def do_EOF(self, line):
        print('Goodbye!')
        return True

    def do_exit(self, line):
        print('Goodbye, normal person!')
        return True

if __name__ == '__main__':
    Calculator().cmdloop()
