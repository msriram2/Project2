#DO NOT USE COLLECTIONS
from keyword import kwlist

def mynamedtuple(type_name, field_names, mutable=False, defaults={}):
    """
    GOAL: The goal of this function is to dynamically generate and simulate a namedtuple by dynamically generating classes
    with the exec() function.

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
        def dup(field_names):
            for i in range(len(field_names)):
                for j in range(i + 1, len(field_names)):
                    if field_names[i] == field_names[j]:
                        field_names.remove(field_names[j])
            return field_names
        new_fields = filter(dup, field_names)
        Class = mynamedtuple(f'{type_name}', new_fields, mutable, defaults)

        yield Class


if __name__ == '__main__':
    classes = mynamedtuple()
















