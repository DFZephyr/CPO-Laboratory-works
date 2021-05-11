

import unittest
from hypothesis import given
import hypothesis.strategies as st

from Hashmap_immutable import *
import Hashmap


class TestMutableList(unittest.TestCase):
    def test_size_and_put(self):
        h = Hashmap.Set()
        self.assertEqual(size(h), 0)
        put(1, "1", h)

        self.assertEqual(size(h), 1)
        put(1,"1", h)
        put(1,"1", h)
        put(1,"1", h)
        put(2,"2", h)
        self.assertEqual(size(h), 2)
    def test_find(self):
        h = Hashmap.Set()
        self.assertEqual(size(h), 0)
        put(1, "1", h)
        self.assertEqual(size(h), 1)
        put(2, "2", h)
        self.assertEqual(size(h), 2)
        self.assertEqual(find(1, h), "1")
        self.assertEqual(find(2, h), "2")

    def test_remove(self):
        h=Hashmap.Set()
        self.assertEqual(size(h), 0)
        put(1, "1", h)
        self.assertEqual(size(h), 1)
        put(2, "2", h)
        self.assertEqual(size(h), 2)
        remove(1, h)
        self.assertEqual(size(h),1)

    def test_map(self):
        h=Hashmap.Set()
        put(1, 1, h)
        put(2, 2, h)
        put(3, 3, h)
        put(4, -1, h)
        self.assertEqual(size(h), 4)
        map(squre, h)
        self.assertEqual(find(2, h),4)

    def test_reduce(self):
        h=Hashmap.Set()
        put(1, 1, h)
        put(2, 2, h)
        put(3, 3, h)
        put(4, -1, h)
        self.assertEqual(size(h), 4)
        x=reduce(lambda x,y:x+y,0, h)
        self.assertEqual(x, 5)

    def test_to_list(self):
        h = Hashmap.Set()
        put(1, 1, h)
        put(2, 2, h)
        put(3, 3, h)
        put(4, -1, h)
        self.assertEqual(to_list(h), [1,2,3,-1])

    def test_from_list(self):
        res=[1,2,3,-1]
        h = Hashmap.Set()
        from_list(res, h)
        self.assertEqual(size(h), 4)
        self.assertEqual(find(0, h), 1)
        self.assertEqual(find(1, h), 2)

    def test_monoid_identity(self):
        h = Hashmap.Set()
        put(1, 1, h)
        put(2, 2, h)
        put(3, 3, h)
        put(4, -1, h)
        self.assertEqual(mconcat(mempty(h), h, h), h)
        self.assertEqual(mconcat(h, mempty(h), h), h)

    def test_monoid_associativity(self):
        h1 = Hashmap.Set()
        h2 = Hashmap.Set()
        h3 = Hashmap.Set()
        put(1, 1, h1)
        put(2, 2, h1)
        put(3, 3, h2)
        put(4, -1, h3)
        mconcat(h1, h2, h1)
        aa = mconcat(mconcat(h1, h2, h1), h3, h1).to_list()
        bb = mconcat(h1, mconcat(h2, h3, h1), h1).to_list()
        self.assertEqual(aa.sort(), bb.sort())

    def test_filter(self):
        h1 = Hashmap.Set()
        put(1, 1, h1)
        put(2, 2, h1)
        put(3, 3, h1)
        put(5, 6, h1)
        put(6, 8, h1)
        put(4, -1, h1)
        filter(lambda x: x % 2 == 0, h1)
        self.assertEqual(to_list(h1).sort(), [2, 6, 8].sort())

def squre(x):
    return x ** 2

if __name__ == '__main__':
    unittest.main()