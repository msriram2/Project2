#DO NOT USE COLLECTIONS
from keyword import kwlist


def mynamedtuple(type_name, field_names, mutable=False, defaults={}):
    """
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

class coordinate:
    """
    Objective:

    """
    _fields = ['x', 'y']
    _mutable = False

    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    #NOTE: Will have to do a string manipulation?
    #NOTE: Consider difference between (x,y) and (y, x) in context
    # of instances

    def __repr__(self) -> str:
        return 'coordinate('+ ('x='+ self.x, 'y='+ self.y) + ')'
        #Find a way to rewrite this equation with the join. statement
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    #Overloading proper method to overload indexing operator

    def __eq__(self):
        pass

    def _asdict(self):
        pass

    def _make(self, iter):
        pass
    def _replace(self, **kwargs):
        pass

    def __setattr__(self):
        pass


class DictTuple:

    def __init__(self, *args):
        self.arg = args

    def arg_exists(self):
        if self.args == None:
            raise AssertionError('DictTuple.__init__:' + self.args + ' is not a dictionary')

    def __len__(self):
        pass

    def __bool__(self):
        pass

    def __repr__(self):
        pass

    def __contains__(self, **kwargs):
        pass

    #def proper method so that d[k] will return value associated
    # with latest dictionary

    def __iter__(self):
        pass













