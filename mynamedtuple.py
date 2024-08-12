#DO NOT USE COLLECTIONS
from keyword import kwlist


def mynamedtuple(type_name, field_names, mutable=False, defaults={}):
    """
    GOAL: The goal of this function is to dynamically generate and simulate a namedtuple by dynamically generating classes
    with the exec() function.

    WHAT TO KNOW:
    - How to dynamically generate classes
    - How do namedtuples work?
    - How does the exec() function work?


    Questions:
    1) How to get variable name to equal type_name without using collections
    2) How to make sure the program is able to maintain the sequence of the code in field_names?
    3) field_names has to be an iterator, therefore, I need the program to determine if it is an iterator or else it
    should raise a TypeError.
    4) How to filter out duplicate names in field names?

    - field_names can accept a list or string.
    - Make sure I look into Python keywords to use for accepting type and field names.

    :param type_name:
    :param field_names:
    :param mutable:
    :param defaults:
    :return:
    """
    if type_name is not str:
        raise SyntaxError('Wrong type for type_name parameter.')
    if type_name == (item for item in kwlist):
        raise SyntaxError('type_name corresponds to keyword in kwlist.')
    if field_names is not list or str:
        raise SyntaxError('Wrong type for field_names parameter')
    for i in range(len(defaults)):
        for j in range(len(field_names)):
            if defaults[i] != field_names[j]:
                raise SyntaxError('Defaults do not match field names.')
    else:
        """Either use list comprehension or filter method. Now trying filter"""
        def dup(field_names):
            for i in range(len(field_names)):
                for j in range(i + 1, len(field_names)):
                    if field_names[i] == field_names[j]:
                        field_names.remove(field_names[j])
            return field_names
        new_fields = filter(dup, field_names)
        Class = mynamedtuple(f'{type_name}', new_fields, mutable, defaults)
        #There's the potential of having to include a generator function. Figure out how to integrate that.

class DictTuple:
    """
    Goal: Ones the tuples are created by the mynamedtuples generative function, the goal of DictTuple is to store
    these namedtuples using keys and support operator overloading.

    WHAT TO KNOW:
    - Review operator overloading
    """

    def __init__(self, *args:dict):
        for arg in args:
            if arg == None:
                raise AssertionError('There are no dictionary arguments.')
            if type(arg) is not dict:
                raise AssertionError('One ore more arguments is not a dictionary.')
            if arg == "":
                raise AssertionError("One or more dictionaries are empty.")
        else:
            self.dt = args

    def __len__(self):
        num_of_keys = 0
        for i in range(len(self.dt)):
            for j in range(len(self.dt)):
                if i != j:
                    num_of_keys += 1

    def __bool__(self):
        if len(self.dt) == 1:
            return False
        if len(self.dt) > 1:
            return True

    def __repr__(self):
        #Review string representation
        return "DictTuple(" + self.dt.join()+  ")"

    def __contains__(self, **kwargs):
        pass

    #def proper method so that d[k] will return value associated
    # with latest dictionary

    def __iter__(self):
        pass













