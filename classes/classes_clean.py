"""
ex of how an object wraps a list, and for the methods we are interested in, we just delegate to its corresponding version on the list object:"""

from _collections_abc import Sequence

class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

"""
this ex uses composition (because it contains an internal collaborator that is a list rather than inheriting from the list class

another way of doing it is through class inheritance - in which case you will have to extend collections.UserList base class"""