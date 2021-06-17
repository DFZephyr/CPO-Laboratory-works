from SingleLinkList import *
import unittest


class TestSingleLinkList(unittest.TestCase):
    def test_head(self):
        self.assertEqual(head(initNode(1, None)), 1)
        self.assertEqual(head(initNode(1, initNode(2, initNode(3, initNode(4, None))))), 1)

    def test_tail(self):
        self.assertEqual(tail(initNode(1, None)), 1)
        self.assertEqual(tail(initNode(1, initNode(2, initNode(3, initNode(4, None))))), 4)

    def test_take(self):
        self.assertEqual(take(initNode(1, None), 1), 1)
        self.assertEqual(take(initNode(1, initNode(2, initNode(3, initNode(4, None)))), 2), 2)

    def test_length(self):
        self.assertEqual(length(initNode(1, None)), 1)
        self.assertEqual(length(initNode(1, initNode(2, initNode(3, initNode(4, None))))), 4)

    def test_map(self):
        self.assertEqual(to_list(map(initNode(1, initNode(2, initNode(3, initNode(4, None)))), str)),
                         to_list(initNode("1", initNode("2", initNode("3", initNode("4", None))))))

    def test_reduce(self):

        self.assertEqual(reduce(initNode(1, initNode(2, initNode(3, initNode(4, None)))), lambda count, _: count + 1, 0), 4)
        self.assertEqual(reduce(initNode(1, initNode(2, initNode(3, initNode(4, None)))), lambda sum, e: sum + e, 0), 10)

    def test_empty(self):
        self.assertEqual(empty(), None)

    def test_concat(self):
        self.assertEqual(to_list(concat(initNode(1, None), None)), to_list(initNode(1, None)))
        self.assertEqual(to_list(concat(None, initNode('1', None))), to_list(initNode('1', None)))
        self.assertEqual(to_list(concat(initNode('1', None), initNode('2', initNode('3', None)))), to_list(initNode('1', initNode('2', initNode('3', None)))))

    def test_from_list(self):
        test_lists = [
            [], ['a'], ['a', 'b']
        ]
        for test_list in test_lists:
            new_list = from_list(test_list)
            self.assertEqual(to_list(new_list), test_list)

    def test_to_list(self):
        self.assertEqual(to_list(initNode(1, initNode(2, initNode(3, initNode(4, None))))), [1, 2, 3, 4])
        self.assertEqual(to_list(initNode('a', initNode('b', initNode('c', initNode('d', None))))), ['a', 'b', 'c', 'd'])

    def test_iter(self):
        x = [1, 2, 3]
        lists = from_list(x)
        tmp = []
        try:
            get_next = iterator(lists)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lists), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

if __name__=="__main__":
    unittest.main()