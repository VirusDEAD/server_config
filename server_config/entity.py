# -*- coding: utf-8 -*-


class Entity(dict):
    """
    An entity object. Can be accessed as a dict or as an obj. The attributes of
    the entity will be created dynamically. For example, the following are both
    valid::
        entity = Entity()
        entity.a = 'b'
        entity['x'] = 'y'
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError("Attribute {} for object of type {} is missing".format('Entity', name))

    __setattr__ = dict.__setitem__

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            raise AttributeError("Attribute {} for object of type {} is missing".format('Entity', name))

    def __dir__(self):
        return dir({}) + list(self.keys())

