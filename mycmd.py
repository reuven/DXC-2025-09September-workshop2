#!/usr/bin/env python3

import cmd

class MyCmd(cmd.Cmd):
    def do_say(self, line):
        """Say something to the user"""
        print(f'I am saying: {line}')

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
