import unittest
from hypothesis import given
import hypothesis.strategies as st
import Hashmap
class TestMutableList(unittest.TestCase):
    """"
       One function one for testing because some global variables are set
    """
    def test_size_and_put(self):
        h=Hashmap
        self.assertEqual(h.get_size(), 0)
        h.put(1,"1")
        self.assertEqual(1, h.get_size())
        h.put(2,"2")
        self.assertEqual(h.get_size(), 2)
    # def test_get(self):
    #     h=Hashmap
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    #     h.put(2, "2")
    #     self.assertEqual(h.get_size(), 2)
    #     self.assertEqual(h.getValue(1), "1")
    #     self.assertEqual(h.getValue(2), "2")
    # def test_delete_by_key(self):
    #     h = Hashmap
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    #     h.put(2, "2")
    #     self.assertEqual(h.get_size(), 2)
    #     h.delete_by_key(1)
    #     self.assertEqual(h.get_size(),1)
    # def test_map(self):
    #     h = Hashmap
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.get_size(), 4)
    #     h.map(squre)
    #     self.assertEqual(h.getValue(2),4)
    # def test_reduce(self):
    #     h = Hashmap
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.get_size(), 4)
    #     x=h.reduce(lambda x,y:x+y,0)
    #     print(x)
def squre(x):
    return x ** 2



if __name__ == '__main__':
    unittest.main()