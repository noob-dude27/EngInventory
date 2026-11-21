from src.dsa.linked_list import linked_list

import unittest

class test_normal_cases(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()
        initial_data = [10, 20, 30, 40]
        for i in initial_data:
            self.ll.insert_at_tail(i)

    def test_forward_traversal(self):
        self.assertEqual(self.ll.traverse(), [10, 20, 30, 40])

    def test_backward_traversal(self):
        self.assertEqual(self.ll.traverse(reverse=True), [40, 30, 20, 10])

    def test_insert_at_head(self):
        new_ll = linked_list()
        new_ll.insert_at_head(10)
        new_ll.insert_at_head(20)
        new_ll.insert_at_head(30)
        self.assertEqual(new_ll.traverse(), [30,20,10])

    def test_insert_at_tail(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.insert_at_tail(20)
        new_ll.insert_at_tail(30)
        self.assertEqual(new_ll.traverse(), [10,20,30])

    def test_insert_mixed(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.insert_at_head(20)
        new_ll.insert_at_tail(30)
        new_ll.insert_at_head(40)
        self.assertEqual(new_ll.traverse(), [40,20,10,30])
        
    def test_remove(self):
        # from [10, 20, 30, 40] must be [20, 30]  
        self.assertTrue(self.ll.remove(40), True)
        self.assertFalse(self.ll.remove(50), False)
        self.assertTrue(self.ll.remove(10), True)
        self.assertEqual(self.ll.traverse(), [20,30])


class test_boundary_cases(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()
        initial_data = [10, -30, "Hello world", None, 10.00]
        for i in initial_data:
            self.ll.insert_at_tail(i)

    def test_traversal_with_mixed_elements(self):
        self.assertEqual(self.ll.traverse(), [10, -30, "Hello world", None, 10.00])
        self.assertEqual(self.ll.traverse(reverse=True), [10.00, None, "Hello world", -30, 10])

    def test_single_node_traversal(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        self.assertEqual(new_ll.traverse(), [10])
        self.assertEqual(new_ll.traverse(reverse=True), [10])

    def test_insert_mixed(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.insert_at_head(None)
        new_ll.insert_at_head("My string")
        self.assertEqual(new_ll.traverse(), ["My string", None, 10])

    def test_single_node_removal(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.remove(10)
        self.assertIsNone(new_ll.head, None)
        self.assertIsNone(new_ll.tail, None)
        self.assertEqual(new_ll.size, 0)


class test_edge_cases(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()
        initial_data = [30, 30.00, "30"]
        for i in initial_data:
            self.ll.insert_at_tail(i)

    def test_empty_traversal(self):
        new_ll = linked_list()
        self.assertEqual(new_ll.traverse(), [])
        self.assertEqual(new_ll.traverse(reverse=True), [])

    def test_similar_data_removal(self):
        self.ll.remove(30)
        self.assertEqual(type(self.ll.head.data), type(30.00)) # must return: float == float
        self.ll.insert_at_tail(30)
        self.ll.remove(30.00)
        self.assertEqual(type(self.ll.head.data), type("30")) # must return: str == str
    
    def test_duplicate_data_removal(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.insert_at_tail(10)
        new_ll.insert_at_tail(10)
        new_ll.remove(10)
        self.assertEqual(new_ll.traverse(), [10,10])
        new_ll.remove(10)
        self.assertEqual(new_ll.traverse(), [10])

    def test_pointer_integrity(self):
        # nodes must be [30, 30.00, "30"] through node reference, not just through surface traversal
        nodes = []
        current = self.ll.head

        while current:
            nodes.append(current)
            current = current.next

        for i, node in enumerate(nodes):
            expected_prev = nodes[i - 1] if i > 0 else None
            expected_next = nodes[i + 1] if i < len(nodes) - 1 else None

            self.assertIs(node.prev, expected_prev)
            self.assertIs(node.next, expected_next)

if __name__ == "__main__":
    unittest.main()