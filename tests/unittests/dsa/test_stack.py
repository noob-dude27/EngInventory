# NOTE: ai-generated, will refactor soon

from src.dsa.stack import stack

import unittest

class test_normal_cases(unittest.TestCase):
    def setUp(self):
        self.st = stack()

    def test_push_single(self):
        self.st.push(10)
        self.assertEqual(self.st.peek(), 10)
        self.assertEqual(self.st.size, 1)

    def test_push_multiple(self):
        data = [10,20,30]
        for x in data:
            self.st.push(x)

        self.assertEqual(self.st.size, 3)
        self.assertEqual(self.st.peek(), 30)

    def test_pop_lifo(self):
        data = [10,20,30]
        for x in data:
            self.st.push(x)

        self.assertEqual(self.st.pop(), 30)
        self.assertEqual(self.st.pop(), 20)
        self.assertEqual(self.st.pop(), 10)

    def test_peek_without_removing(self):
        self.st.push(10)
        self.st.push(20)

        self.assertEqual(self.st.peek(), 20)
        self.assertEqual(self.st.size, 2)

class test_boundary_cases(unittest.TestCase):
    def setUp(self):
        self.st = stack()

    def test_pop_single_element(self):
        self.st.push(10)

        self.assertEqual(self.st.pop(), 10)
        self.assertEqual(self.st.size, 0)
        self.assertTrue(self.st.is_empty())

    def test_push_after_empty(self):
        self.st.push(10)
        self.st.pop()

        self.st.push(20)

        self.assertEqual(self.st.peek(), 20)
        self.assertEqual(self.st.size, 1)

    def test_pop_until_empty(self):
        data = [10,20,30]
        for x in data:
            self.st.push(x)

        self.st.pop()
        self.st.pop()
        self.st.pop()

        self.assertTrue(self.st.is_empty())
        self.assertEqual(self.st.size, 0)

class test_edge_cases(unittest.TestCase):
    def setUp(self):
        self.st = stack()

    def test_pop_empty(self):
        self.assertIsNone(self.st.pop())

    def test_peek_empty(self):
        self.assertIsNone(self.st.peek())

    def test_duplicate_values(self):
        data = [10, 10, 20, 10]
        for x in data:
            self.st.push(x)

        self.assertEqual(self.st.pop(), 10)
        self.assertEqual(self.st.pop(), 20)
        self.assertEqual(self.st.pop(), 10)
        self.assertEqual(self.st.pop(), 10)

    def test_falsy_values(self):
        data = [0, False, ""]
        for x in data:
            self.st.push(x)

        self.assertEqual(self.st.pop(), "")
        self.assertIs(self.st.pop(), False)
        self.assertEqual(self.st.pop(), 0)

if __name__ == "__main__":
    unittest.main()