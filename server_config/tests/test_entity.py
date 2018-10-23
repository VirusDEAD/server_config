from unittest import TestCase

from entity import Entity

class TestEntity(TestCase):
    def test_simple_dict(self):
        test_object = {"a": 3 }
        e = Entity(test_object)        
        self.assertTrue(e.a == 3)

    def test_complex_dict(self):
        test_object = {"a": { "b": 3} }
        e = Entity(test_object)        
        self.assertTrue(e.a.b == 3)
