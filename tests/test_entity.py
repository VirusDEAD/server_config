from unittest import TestCase
from nose.tools import raises
from server_config.entity import Entity


class TestEntity(TestCase):

    def test_simple_dict(self):
        data = {"a": 3}
        e = Entity(data)
        self.assertTrue(e.a == 3)

    def test_list(self):
        data = {"list": [1, 2, 3, 4]}
        e = Entity(data)
        self.assertTrue(e.list == [1, 2, 3, 4])

    def test_list_of_dict(self):
        data = {"list": [{"e1": 1}, {"e2": 2}]}
        e = Entity(data)
        self.assertTrue(e.list[0].e1 == 1)

    def test_dict_in_dict(self):
        test_object = {"a": {"b": 3}}
        e = Entity(test_object)
        self.assertTrue(e.a.b == 3)

    @raises(TypeError)
    def test_wrong_type(self):
        test_object = [1, 2]
        Entity(test_object)        
