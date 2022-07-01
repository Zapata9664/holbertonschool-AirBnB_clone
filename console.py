#!/usr/bin/python3
"""Module with class HBNBComman"""
import cmd, sys
from pickle import TRUE


class HBNBCommand(cmd.Cmd):
    """program that contains the entry
    point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the program whit ctrl + D"""
        return True
    
    def do_help(self, arg):
        """Print commands arguments"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        print ("llegue")
        pass

    



if __name__ == '__main__':
    HBNBCommand().cmdloop()