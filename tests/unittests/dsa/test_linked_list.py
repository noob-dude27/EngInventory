# being edited

from src.dsa.linked_list import node, linked_list

import unittest

class test_normal_cases(unittest.TestCase):
    def test_insertion_method(self):
        ll = linked_list()
        ll.insert(10)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.tail.data, 10)

    def test_forward_traversal(self):
        pass

    def test_backward_traversal(self):
        pass

    def test_removal_method(self):
        pass

class test_boundary_cases(unittest.TestCase):
    pass

class test_edge_cases(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()