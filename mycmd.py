#!/usr/bin/env python3

import cmd

class MyCmd(cmd.Cmd):
    def capitalize(self, line):
        return line.capitalize()

    def precmd(self, line):
        if line == 'EOF':
            return line

        parts = line.split()  # turn it into a list of strings
        parts[0] = parts[0].lower()

        return ' '.join(parts)

    def do_say(self, line):
        """Say something to the user"""
        print(f'I am saying: {self.capitalize(line)}')

    def do_EOF(self, line):
        """quit"""
        print('Goodbye!')
        return True

    def do_exit(self, line):
        """quit like a non-Unix head"""
        print('Goodbye, normal person!')
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
