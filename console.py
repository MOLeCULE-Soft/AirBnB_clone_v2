#!/usr/bin/python3
"""Console Module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import shlex
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import json


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class implementation inheriting from cmd.Cmd"""

    prompt = '(hbnb) '

    def class_check(self, arg=None):
        """Check if a given class exists."""
        if arg:
            try:
                tokens = self.parseline(arg)
                eval(tokens[0]).__class__
                return True
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False

    def do_create(self, arg):
        """Create a new instance of a class."""
        if self.class_check(arg):
            new_obj = eval(arg)()
            storage.new(new_obj)
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Display the string representation of an instance."""
        if self.class_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                obj = storage.all()[f"{tokens[0]}.{tokens[1]}"]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if self.class_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                del storage.all()[f"{tokens[0]}.{tokens[1]}"]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Display all instances or all instances of a specific class."""
        if arg:
            if not self.class_check(arg):
                return
        obj_list = []
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(arg):
                    obj_list.append(str(obj))
            else:
                obj_list.append(str(obj))
        print(obj_list)

    def do_count(self, arg):
        """Count the instances of a class."""
        if arg:
            if not self.class_check(arg):
                return
        count = 0
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(arg):
                    count += 1
            else:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update an instance attribute or create a new instance."""
        if self.class_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                attribs = shlex.split(tokens[1])
                obj = storage.all()[f"{tokens[0]}.{attribs[0]}"]
                if len(attribs) > 1:
                    if len(attribs) > 2:
                        setattr(obj, attribs[1], attribs[2])
                        storage.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            except KeyError:
                print("** no instance found **")

    def default(self, line):
        """Handle unrecognized commands."""

        pattern_generic = re.compile(r'^.*\..*\(\)$')
        pattern_with_id = re.compile(r'^.*\..*\(".*"\)$')
        pattern_with_attr = re.compile(r'^.*\..*\(".*",\s+".*",\s+.*\)$')
        pattern_with_dict = re.compile(r'^.*\..*\(".*",\s+\{.*\}\)$')

        if pattern_generic.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            self.onecmd(f"{command} {model}")
        elif pattern_with_dict.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            pattern = re.compile(r'\(.*\)')
            args = pattern.search(line).group(0).strip("()").split(",")
            id = args[0].strip('"')
            start = len(command) + len(model) + len(id) + 5
            dict = line[start:-1].replace("'", '"')
            print(dict)
            dict = json.loads(dict)
            for key in dict.keys():
                attr = key
                val = dict.get(key)
                self.onecmd(f"{command} {model} {id} {attr} {val}")
        elif pattern_with_attr.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            pattern = re.compile(r'\(.*\)')
            args = pattern.search(line).group(0).strip("()").split(",")
            id = args[0].strip('"')
            attr = args[1]
            val = args[2]
            self.onecmd(f"{command} {model} {id} {attr} {val}")
        elif pattern_with_id.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            pattern = re.compile(r'".*"')
            id = pattern.search(line).group(0).strip('"')
            self.onecmd(f"{command} {model} {id}")
        else:
            print(f"Command not recognized: {line}")

    def do_EOF(self, arg):
        """Exit the console on EOF.\n"""
        exit()

    def do_quit(self, arg):
        """Exit the console."""
        exit()

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
