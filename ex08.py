#!/usr/bin/env python3

import cmd

class Calculator(cmd.Cmd):
    def line_to_numbers(self, line):
        numbers = [int(one_number)
                   for one_number in line.split()]
        print(f'{numbers=}')
        return numbers

    def do_add(self, line):
        numbers = self.line_to_numbers(line)
        result = numbers[0] + numbers[1]
        print(f'{numbers[0]} + {numbers[1]} = {result}')

    def do_sub(self, line):
        numbers = self.line_to_numbers(line)
        result = numbers[0] - numbers[1]
        print(f'{numbers[0]} - {numbers[1]} = {result}')

    def do_mul(self, line):
        numbers = self.line_to_numbers(line)
        result = numbers[0] * numbers[1]
        print(f'{numbers[0]} * {numbers[1]} = {result}')

    def do_div(self, line):
        numbers = self.line_to_numbers(line)
        result = numbers[0] / numbers[1]
        print(f'{numbers[0]} / {numbers[1]} = {result}')


    def do_EOF(self, line):
        print('Goodbye!')
        return True

    def do_exit(self, line):
        print('Goodbye, normal person!')
        return True

if __name__ == '__main__':
    Calculator().cmdloop()
