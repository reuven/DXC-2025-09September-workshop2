#!/usr/bin/env python3

import cmd

class MyCmd(cmd.Cmd):
    def do_say(self, line):
        print(f'I am saying: {line}')

    def do_EOF(self, line):
        print('Goodbye!')
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
