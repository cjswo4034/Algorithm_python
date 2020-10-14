class Command(dict):
    def __init__(self, id):
        self.__setitem__('elevator_id', id)

    def set_cmd(self, cmd, idx=None):
        self.__setitem__('command', cmd)
        if idx: self.__setitem__('call_ids', idx)

    def __repr__(self):
        return super().__repr__()

    def __iter__(self):
        return super().__iter__()

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __getitem__(self, key):
        return super().__getitem__(key)