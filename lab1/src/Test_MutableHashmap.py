import copy
import unittest

from hypothesis import given
from collections import Counter
import hypothesis.strategies as st
import pytest
import Hashmap
class TestMutableList(unittest.TestCase):
    def test_size_and_put(self):
        h=Hashmap.Set()
        self.assertEqual(h.get_size(), 0)
        h.add(1,"1")
        self.assertEqual(h.get_size(), 1)
        h.add(1,"1")
        h.add(1,"1")
        h.add(1,"1")
        h.add(2,"2")
        self.assertEqual(h.get_size(), 2)
    def test_find(self):
        h=Hashmap.Set()
        self.assertEqual(h.get_size(), 0)
        h.add(1, "1")
        self.assertEqual(h.get_size(), 1)
        h.add(2, "2")
        self.assertEqual(h.get_size(), 2)
        self.assertEqual(h.find(1), "1")
        self.assertEqual(h.find(2), "2")
    def test_remove(self):
        h=Hashmap.Set()
        self.assertEqual(h.get_size(), 0)
        h.add(1, "1")
        self.assertEqual(h.get_size(), 1)
        h.add(2, "2")
        self.assertEqual(h.get_size(), 2)
        h.remove(1)
        self.assertEqual(h.get_size(),1)
    def test_map(self):
        h=Hashmap.Set()
        h.add(1, 1)
        h.add(2, 2)
        h.add(3, 3)
        h.add(4, -1)
        self.assertEqual(h.get_size(), 4)
        h.map(squre)
        self.assertEqual(h.find(2),4)
    def test_reduce(self):
        h=Hashmap.Set()
        h.add(1, 1)
        h.add(2, 2)
        h.add(3, 3)
        h.add(4, -1)
        self.assertEqual(h.get_size(), 4)
        x=h.reduce(lambda x,y:x+y,0)
        self.assertEqual(x, 5)
    def test_to_list(self):
        def compare(s, t): #Judge whether two lists contain the same elements
            return Counter(s) == Counter(t)
        h = Hashmap.Set()
        h.add(1)
        self.assertEqual(compare(h.to_list(), [1]), True)
        h.add(2)
        self.assertEqual(compare(h.to_list(), [1, 2]), True)

    def test_from_list(self):
        res=[1,2,3]
        h_from_list = Hashmap.Set()
        h_from_list=h_from_list.from_list(res)

        h= Hashmap.Set()
        h.add(1)
        h.add(2)
        h.add(3)
        self.assertEqual(h_from_list.hashmap, h.hashmap)

    def test_monoid_identity(self):
        h = Hashmap.Set()
        h.add(1, 1)
        h.add(2, 2)
        h.add(3, 3)
        h.add(4, -1)
        self.assertEqual(h.mconcat(h.mempty(), h), h)
        self.assertEqual(h.mconcat(h, h.mempty()), h)
    def test_monoid_associativity(self):
        h1 = Hashmap.Set()
        h2 = Hashmap.Set()
        h3 = Hashmap.Set()
        h1_copy=copy.deepcopy(h1)
        h1.add(1, 1)
        h1.add(2, 2)
        h2.add(3, 3)
        h3.add(4, -1)
        h1=h1.mconcat(h1, h2) #h1 h2
        h1 = h1.mconcat(h1,h3) ##(h1 h2) h3

        h2 =h2.mconcat(h2,h3) ##h2 h3
        h1_copy=h2.mconcat(h1,h2)##h1 (h2 h3)
        self.assertEqual(h1.hashmap,h1_copy.hashmap)

    def test_filter(self):
        h1 = Hashmap.Set()
        h1.add(1, 1)
        h1.add(2, 2)
        h1.add(3, 3)
        h1.add(5, 6)
        h1.add(6, 8)
        h1.add(4, -1)
        h1.filter(lambda x: x % 2 == 0)
        self.assertEqual(h1.to_list().sort(), [2, 6 , 8].sort())
def squre(x):
    return x ** 2



if __name__ == '__main__':
    unittest.main()