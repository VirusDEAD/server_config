# -*- coding: utf-8 -*-

"""
Consider using 
https://pypi.org/project/attrdict/
"""

class Entity(dict):
    """
    Class to create attributes for dictionary fields
    Inspired by https://stackoverflow.com/a/3031270/1722325
    Added list capability in __setitem__
    Supports creating Entitys recursively
    """
    MARKER = object()

    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])        
        else:
            raise TypeError('expected dict')

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, Entity):
            value = Entity(value)
        elif isinstance(value, list):
            value = [Entity(o) if (isinstance(o, dict)) else o for o in value]
        super(Entity, self).__setitem__(key, value)

    def __getitem__(self, key):
        found = self.get(key, Entity.MARKER)
        if found is Entity.MARKER:
            found = Entity()
            super(Entity, self).__setitem__(key, found)
        return found

    __setattr__, __getattr__ = __setitem__, __getitem__
