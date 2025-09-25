#!/usr/bin/env python3

import cmd
import calc_extensions

class Calculator(cmd.Cmd):
    def line_to_numbers(self, line):
        numbers = [int(one_number)
                   for one_number in line.split()]
        print(f'{numbers=}')
        return numbers

    def precmd(self, line):
        ops = {'+':'add',
               '-':'sub',
               '*':'mul',
               '/':'div'}

        parts = line.split()
        if parts[0] in ops:
            parts[0] = ops[parts[0]]

        return ' '.join(parts)

    def do_add(self, line):
        """Add two numbers"""
        numbers = self.line_to_numbers(line)
        result = numbers[0] + numbers[1]
        print(f'{numbers[0]} + {numbers[1]} = {result}')

    def do_sub(self, line):
        """Subtract two numbers"""
        numbers = self.line_to_numbers(line)
        result = numbers[0] - numbers[1]
        print(f'{numbers[0]} - {numbers[1]} = {result}')

    def do_mul(self, line):
        """Multiply two numbers"""
        numbers = self.line_to_numbers(line)
        result = numbers[0] * numbers[1]
        print(f'{numbers[0]} * {numbers[1]} = {result}')

    def do_div(self, line):
        """Divide two numbers"""
        numbers = self.line_to_numbers(line)
        result = numbers[0] / numbers[1]
        print(f'{numbers[0]} / {numbers[1]} = {result}')

    def do_EOF(self, line):
        """Quit like a Unix geek"""
        print('Goodbye!')
        return True

    def do_exit(self, line):
        """Quit like a normal person"""
        print('Goodbye, normal person!')
        return True

if __name__ == '__main__':
    def square(self, line):
        """Get the square of a number"""
        numbers = self.line_to_numbers(line)
        result = numbers[0] ** 2
        print(f'{numbers[0]} ** 2 = {result}')

    # Calculator.do_square = square
    # setattr(Calculator, 'do_square', square)
    setattr(Calculator, 'do_square', lambda self, line: print(f'{self.line_to_numbers(line)[0] ** 2}'))

    for function_name in dir(calc_extensions):
        one_function = getattr(calc_extensions, function_name)

        if callable(one_function):
            print(f'{function_name=}')
            setattr(Calculator, f'do_{one_function}', one_function)

    Calculator().cmdloop()
