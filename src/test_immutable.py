import unittest
from hypothesis import given
import hypothesis.strategies as st
import Hashmap_immutable
class TestMutableList(unittest.TestCase):
    """"
       One function one for testing because some global variables are set
    """
    # def test_size_and_put(self):
    #     h=Hashmap_immutable
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1,"1")
    #     self.assertEqual(1, h.get_size())
    #     h.put(2,"2")
    #     self.assertEqual(h.get_size(), 2)
    # def test_add(self):
    #     h = Hashmap_immutable
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    # def test_find(self):
    #     h=Hashmap_immutable
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    #     h.put(2, "2")
    #     self.assertEqual(h.get_size(), 2)
    #     self.assertEqual(h.find(1), "1")
    #     self.assertEqual(h.find(2), "2")
    # def test_get(self):
    #     h=Hashmap_immutable
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    #     h.put(2, "2")
    #     self.assertEqual(h.get_size(), 2)
    #     self.assertEqual(h.getValue(1), "1")
    #     self.assertEqual(h.getValue(2), "2")
    # def test_delete_by_key(self):
    #     h = Hashmap_immutable
    #     self.assertEqual(h.get_size(), 0)
    #     h.put(1, "1")
    #     self.assertEqual(h.get_size(), 1)
    #     h.put(2, "2")
    #     self.assertEqual(h.get_size(), 2)
    #     h.delete_by_key(1)
    #     self.assertEqual(h.get_size(),1)
    # def test_map(self):
    #     h = Hashmap_immutable
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.get_size(), 4)
    #     h.map(squre)
    #     self.assertEqual(h.getValue(2),4)
    # def test_reduce(self):
    #     h = Hashmap_immutable
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.get_size(), 4)
    #     x=h.reduce(lambda x,y:x+y,0)
    #     print(x)
    # def test_to_list(self):
    #     h = Hashmap_immutable
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.to_list(), [1,2,3,-1])
    # def test_from_list(self):
    #     res=[1, 2, 3, -1]
    #     h = Hashmap_immutable
    #     h.from_list(res)
    #     self.assertEqual(h.get_size(), 4)
    #     a=h.find(0)
    #     self.assertEqual(h.find(0), 1)
    #     self.assertEqual(h.find(1), 2)
    # def test_monoid_identity(self):
    #     h = Hashmap_immutable
    #     h.put(1, 1)
    #     h.put(2, 2)
    #     h.put(3, 3)
    #     h.put(4, -1)
    #     self.assertEqual(h.mconcat(h, h), True)

    # def test_filter(self):
    #     h1 = Hashmap_immutable
    #     h1.put(1, 1)
    #     h1.put(2, 2)
    #     h1.put(3, 3)
    #     h1.put(5, 6)
    #     h1.put(6, 8)
    #     h1.put(4, -1)
    #     h1.filter(lambda x: x % 2 == 0)
    #     self.assertEqual(h1.to_list().sort(), [6 , 8].sort())
def squre(x):
    return x ** 2



if __name__ == '__main__':
    TestMutableList.test_monoid_associativity()
