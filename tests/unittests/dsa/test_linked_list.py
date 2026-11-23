# Test by: EZRA FORTUNADO
# TODO: Improve readability of code

from src.dsa.linked_list import linked_list, node

import unittest

class test_normal_cases(unittest.TestCase):
    def setUp(self):
        # pretend I did not copy from insert_at_tail method
        self.ll = linked_list()
        self.initial_data = [10, 20, 30, 40]
        self.ll.size = len(self.initial_data)

        for data in self.initial_data:
            new = node(data)

            if self.ll.head == None:
                self.ll.head = new
                self.ll.tail = new
            else:
                self.ll.tail.next = new
                new.prev = self.ll.tail
                self.ll.tail = new

    def test_forward_traversal(self):
        self.assertEqual(self.ll.traverse(), [10, 20, 30, 40])

    def test_backward_traversal(self):
        self.assertEqual(self.ll.traverse(reverse=True), [40, 30, 20, 10])

    def test_insert_at_head(self):
        new_ll = linked_list()
        data = [10,20,30]
        for i in data:
            new_ll.insert_at_head(i)

        self.assertEqual(new_ll.traverse(), [30,20,10])

    def test_insert_at_tail(self):
        new_ll = linked_list()
        data = [10,20,30]
        for i in data:
            new_ll.insert_at_tail(i)
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
        self.assertTrue(self.ll.remove(40))
        self.assertFalse(self.ll.remove(50))
        self.assertTrue(self.ll.remove(10))
        self.assertEqual(self.ll.traverse(), [20,30])

    def test_remove_at_head(self):
        self.ll.remove_at_head()
        self.assertEqual(self.ll.traverse(), [20,30,40])
        self.assertEqual(self.ll.head.data, 20)

        self.ll.remove_at_head()
        self.assertEqual(self.ll.traverse(), [30,40])
        self.assertEqual(self.ll.head.data, 30)

    def test_remove_at_tail(self):
        self.ll.remove_at_tail()
        self.assertEqual(self.ll.traverse(), [10,20,30])
        self.assertEqual(self.ll.tail.data, 30)

        self.ll.remove_at_tail()
        self.assertEqual(self.ll.traverse(), [10,20])
        self.assertEqual(self.ll.tail.data, 20)

    def test_clear(self):
        self.ll.clear()
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.tail, None)
        self.assertEqual(self.ll.size, 0)
        self.assertEqual(self.ll.traverse(), [])

    def test_update_at_first(self):
        self.ll.update_at_first(10, 60)
        self.assertEqual(self.ll.traverse(), [60, 20, 30, 40])

    
class test_boundary_cases(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()
        self.initial_data = [10, -30, "Hello world", None, 10.00]
        self.ll.size = len(self.initial_data)
        for data in self.initial_data:
            new = node(data)

            if self.ll.head == None:
                self.ll.head = new
                self.ll.tail = new
            else:
                self.ll.tail.next = new
                new.prev = self.ll.tail
                self.ll.tail = new

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
        new_ll.insert_at_tail([5,9])
        self.assertEqual(new_ll.traverse(), ["My string", None, 10, [5,9]])

    def test_single_node_removal(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(10)
        new_ll.remove(10)
        self.assertIsNone(new_ll.head, None)
        self.assertIsNone(new_ll.tail, None)
        self.assertEqual(new_ll.size, 0)

    def test_empty_clear(self):
        new_ll = linked_list()
        new_ll.clear()
        self.assertEqual(new_ll.head, None)
        self.assertEqual(new_ll.tail, None)
        self.assertEqual(new_ll.size, 0)
        self.assertEqual(new_ll.traverse(), [])

    def test_update_duplicate(self):
        new_ll = linked_list()
        for _ in range(3):
            new_ll.insert_at_tail(10)
        for i in range(3):
            self.assertTrue(new_ll.update_at_first(10, i)) # should return [1,2,3]

    def test_single_remove_at(self):
        new_ll = linked_list()
        new_ll.insert_at_tail("single")
        new_ll.remove_at_tail()

        self.assertEqual(new_ll.traverse(), [])
        self.assertIsNone(new_ll.head)
        self.assertIsNone(new_ll.tail)

class test_edge_cases(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()
        self.initial_data = [30, 30.00, "30", [30, 30]]
        self.ll.size = len(self.initial_data)
        for data in self.initial_data:
            new = node(data)

            if self.ll.head == None:
                self.ll.head = new
                self.ll.tail = new
            else:
                self.ll.tail.next = new
                new.prev = self.ll.tail
                self.ll.tail = new

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
        for i in range(3):
            new_ll.insert_at_head(10)
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

    def test_update_nonetype(self):
        new_ll = linked_list()
        new_ll.insert_at_tail(None)
        self.assertTrue(new_ll.update_at_first(None, "something"))

    def test_update_not_existing(self):
        new_ll = linked_list()
        self.assertFalse(new_ll.update_at_first(None, "something"))

    def test_update_diff_type(self):
        pass

    def test_empty_remove_at(self):
        new_ll = linked_list()
        new_ll.remove_at_tail()
        self.assertEqual(new_ll.traverse(), [])
        self.assertIsNone(new_ll.head)
        self.assertIsNone(new_ll.tail)

if __name__ == "__main__":
    unittest.main()