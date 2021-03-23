import unittest
from hypothesis import given
import hypothesis.strategies as st
import Hashmap
class TestMutableList(unittest.TestCase):
    def test_size_and_put(self):
        h=Hashmap.HashMap()
        self.assertEqual(h.get_size(), 0)
        h.put(1,"1")
        self.assertEqual(h.get_size(), 1)
        h.put(2,"2")
        self.assertEqual(h.get_size(), 2)
    def test_get(self):
        h=Hashmap.HashMap()
        self.assertEqual(h.get_size(), 0)
        h.put(1, "1")
        self.assertEqual(h.get_size(), 1)
        h.put(2, "2")
        self.assertEqual(h.get_size(), 2)
        self.assertEqual(h.getValue(1), "1")
        self.assertEqual(h.getValue(2), "2")
    def test_delete_by_key(self):
        h = Hashmap.HashMap()
        self.assertEqual(h.get_size(), 0)
        h.put(1, "1")
        self.assertEqual(h.get_size(), 1)
        h.put(2, "2")
        self.assertEqual(h.get_size(), 2)
        h.delete_by_key(1)
        self.assertEqual(h.get_size(),1)
    def test_map(self):
        h = Hashmap.HashMap()
        h.put(1, 1)
        h.put(2, 2)
        h.put(3, 3)
        h.put(4, -1)
        self.assertEqual(h.get_size(), 4)
        h.map(squre)
        self.assertEqual(h.getValue(2),4)
    def test_reduce(self):
        h = Hashmap.HashMap()
        h.put(1, 1)
        h.put(2, 2)
        h.put(3, 3)
        h.put(4, -1)
        self.assertEqual(h.get_size(), 4)
        x=h.reduce(lambda x,y:x+y,0)
        self.assertEqual(x, 5)
def squre(x):
    return x ** 2



if __name__ == '__main__':
    unittest.main()