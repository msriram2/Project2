from mynamedtuple import mynamedtuple
class DictTuple:
    """
    Goal: Ones the tuples are created by the mynamedtuples generative function, the goal of DictTuple is to store
    these namedtuples using keys and support operator overloading.

    """

    def __init__(self, *args:dict):
        for arg in args:
            if arg == ():
                raise AssertionError()
            if type(arg) != dict:
                raise AssertionError()
            if arg == "":
                raise AssertionError()
        else:
            self.dt = args
            print(self.dt)

    def __len__(self):
        key_list = []
        for dicts in self.dt:
            for key in dicts:
                key_list.append(key)
                print(key_list)
        key_list = list(set(key_list))

        return len(key_list)

    def __bool__(self):
        if len(self.dt) == 1:
            return False
        if len(self.dt) > 1:
            return True

    def __repr__(self):
        return "DictTuple(" + ','.join(str(dicts) for dicts in self.dt) + ")"

    def __contains__(self, item):
        return any(key == item for dicts in self.dt for key in dicts)

    def __getitem__(self, k):
        for dicts in self.dt:
            for key, value in dicts:
                if key[-1:] == k:
                    return key

    def __setitem__(self, k, v):
        for dicts in self.dt:
            for key, value in dicts:
                if key[-1] == k:
                    dicts[key] = v
                if key != k:
                    new_dict = {}
                    new_dict[k] = v
                    self.dt.append(new_dict)

    def __del__(self, k):
        for dict in self.dt:
            for key, value in dict:
                if key == k:
                    self.dt.remove(key)
                if key != k:
                    raise KeyError('Cannot find key in any dictionary')

    def __enter__(self, k):
        key_list = []
        for dict in self.dt:
            for key, value in dict:
                if key == k:
                    key_list.append(key)
                    return key_list
                else:
                    return ['']

    def __iter__(self):
        sorted_keys = []
        for dicts in self.dt:
            for key in dicts:
                sorted_keys.append(key[-1])
        sorted_keys = list(set(sorted_keys))
        new_sorted_keys = reversed(sorted(sorted_keys))
        return new_sorted_keys

