#!/usr/bin/python3
"""Module with class HBNBComman"""
import cmd
import sys
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.user import User

classtype = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


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
        print("llegue")
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it and prints the id"""
        tokens = arg.split()

        if len(tokens) == 0:
            print("** class name missing **")

        else:
            if tokens[0] in classtype:
                insmbase = classtype[tokens[0]]()
                print(insmbase.id)
                insmbase.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        tokens = arg.split()

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classtype:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        userfile = open("file.json", "r")
        print(userfile.read())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
