#!/usr/bin/env python3

import cmd

class MyCmd(cmd.Cmd):
    def do_say(self, line):
        print(f'I am saying: {line}')

if __name__ == '__main__':
    MyCmd().cmdloop()
