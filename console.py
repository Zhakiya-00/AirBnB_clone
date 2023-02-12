#!/usr/bin/python3
"""A program that contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Define class HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to end the program"""
        return True

    def emptyline(self):

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
