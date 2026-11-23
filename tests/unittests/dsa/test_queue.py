# NOTE: ai-generated, will refactor soon
from src.dsa.queue import queue

import unittest

class test_normal_cases(unittest.TestCase):
    def setUp(self):
        self.q = queue()

    def test_enqueue_single(self):
        self.q.enqueue(10)

        self.assertEqual(self.q.peek(), 10)
        self.assertEqual(self.q.size, 1)

    def test_enqueue_multiple(self):
        data = [10,20,30]
        for x in data:
            self.q.enqueue(x)

        self.assertEqual(self.q.size, 3)
        self.assertEqual(self.q.peek(), 10)

    def test_dequeue_fifo(self):
        data = [10,20,30]
        for x in data:
            self.q.enqueue(x)

        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.dequeue(), 20)
        self.assertEqual(self.q.dequeue(), 30)

    def test_peek_without_removing(self):
        self.q.enqueue(10)
        self.q.enqueue(20)

        self.assertEqual(self.q.peek(), 10)
        self.assertEqual(self.q.size, 2)

class test_boundary_cases(unittest.TestCase):
    def setUp(self):
        self.q = queue()

    def test_dequeue_single_element(self):
        self.q.enqueue(10)

        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.size, 0)
        self.assertTrue(self.q.is_empty())

    def test_enqueue_after_empty(self):
        self.q.enqueue(10)
        self.q.dequeue()

        self.q.enqueue(20)

        self.assertEqual(self.q.peek(), 20)
        self.assertEqual(self.q.size, 1)

    def test_dequeue_until_empty(self):
        data = [10,20,30]
        for x in data:
            self.q.enqueue(x)

        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()

        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size, 0)

class test_edge_cases(unittest.TestCase):
    def setUp(self):
        self.q = queue()

    def test_dequeue_empty(self):
        self.assertIsNone(self.q.dequeue())

    def test_peek_empty(self):
        self.assertIsNone(self.q.peek())

    def test_duplicate_values(self):
        data = [10, 10, 20, 10]
        for x in data:
            self.q.enqueue(x)

        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.dequeue(), 20)
        self.assertEqual(self.q.dequeue(), 10)

    def test_falsy_values(self):
        data = [0, False, ""]
        for x in data:
            self.q.enqueue(x)

        self.assertEqual(self.q.dequeue(), 0)
        self.assertIs(self.q.dequeue(), False)
        self.assertEqual(self.q.dequeue(), "")

if __name__ == "__main__":
    unittest.main()