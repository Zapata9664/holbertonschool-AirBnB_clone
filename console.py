#!/usr/bin/python3
"""Module with class HBNBComman"""
import cmd
import sys
from unittest import installHandler
from venv import create
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import json

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
        objectDic = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classtype:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] + "." + tokens[1] in objectDic:
            print(objectDic[tokens[0] + "." + tokens[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        tokens = arg.split()
        objectDic = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classtype:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] + "." + tokens[1] in objectDic.keys():
            del objectDic[tokens[0] + "." + tokens[1]]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class name"""
        tokens = arg.split()
        if len(tokens) > 0 and tokens[0] not in classtype:
            print("** class doesn't exist **")
        else:
            new_list = []
            for obj in storage.all().values():
                if len(tokens) > 0 and tokens[0] == obj.__class__.__name__:
                    new_list.append(obj.__str__())
                elif len(tokens) == 0:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        tokens = arg.split()
        objectDic = storage.all()

        ints = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
        floats = ["latitude", "longitude"]

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] in classtype:
            if len(tokens) > 1:
                if tokens[0] + "." + tokens[1] in objectDic:
                    if len(tokens) > 2:
                        if len(tokens) > 3:
                            if tokens[0] == "Place":
                                if tokens[2] in ints:
                                    try:
                                        tokens[3] = int(tokens[3])
                                    except Exception:
                                        tokens[3] = 0
                                elif tokens[2] in floats:
                                    try:
                                        tokens[3] = float(tokens[3])
                                    except Exception:
                                        tokens[3] = 0.0
                            setattr(objectDic[tokens[0] + "." + tokens[1]],
                                    tokens[2], tokens[3])
                            objectDic[tokens[0] + "." + tokens[1]].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
