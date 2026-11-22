# Test by: EZRA FORTUNADO
# TODO: Improve readability of code, learn how to write better tests cuz this sucks

from src.dsa.hash_table import hash_table
from src.dsa.linked_list import linked_list

import unittest

class test_normal_cases(unittest.TestCase):
    def setUp(self):
        self.ht = hash_table()

    def test_init_default(self):
        new_ht = hash_table()
        self.assertTrue(type(new_ht.buckets[0]), type(linked_list()))
        self.assertEqual(new_ht.buckets[0].size, 0)

    def test_init_custom(self):
        new_ht = hash_table(10, 1)
        for i in range(10):
            self.assertTrue(type(new_ht.buckets[i]), type(linked_list()))
            self.assertEqual(new_ht.buckets[i].size, 0)

    def test_insert_single(self):
        self.assertTrue(self.ht.insert("Hello", "World"))
        self.assertEqual(self.ht.contains("Hello"), "World")

    def test_insert_multiple(self):
        self.assertTrue(self.ht.insert("Hello", "World")) # Hello -> World
        self.assertTrue(self.ht.insert("Goodbye", "Now")) # Goodbye -> Now
        self.assertTrue(self.ht.insert("Computer", "Engineering")) # Computer -> Engineering
        
        self.assertEqual(self.ht.contains("Hello"), "World")
        self.assertEqual(self.ht.contains("Goodbye"), "Now")
        self.assertEqual(self.ht.contains("Computer"), "Engineering")

    def test_element_count(self):
        self.ht.insert("A", 1)
        self.ht.insert("B", 2)
        self.assertEqual(self.ht.element_count, 2)

        self.ht.remove("A")
        self.assertEqual(self.ht.element_count, 1)

    def test_retrieval(self):
        self.assertTrue(self.ht.insert("Hello", "World"))
        self.assertEqual(self.ht.contains("Hello"), "World")

    def test_remove_existing(self):
        self.assertTrue(self.ht.insert("Hello", "World"))
        self.assertTrue(self.ht.insert("Goodness", "Gracious"))

        self.assertTrue(self.ht.remove("Hello"))
        self.assertTrue(self.ht.remove("Goodness"))

    def test_update(self):
        pass


class test_boundary_cases(unittest.TestCase):
    def setUp(self):
        ht_size = 1
        load_factor = 1000 # I set this to an impossible value to force collision
        self.ht = hash_table(ht_size, load_factor)

    def test_init_size_zero(self):
        with self.assertRaises(ValueError):
            hash_table(0)
        
    def test_insert_collision(self):
        self.ht.insert("Hello", "World")
        self.ht.insert("Hey", "There")
        self.assertEqual(self.ht.peek(0), [["Hello", "World"], ["Hey", "There"]])

    def test_retrieve_at_empty(self):
        self.assertFalse(self.ht.contains("Hello"))

    def test_retrieve_collision(self):
        self.ht.insert("Hello", "World")
        self.ht.insert("Hey", "There")

        self.assertEqual(self.ht.contains("Hello"), "World")
        self.assertEqual(self.ht.contains("Hey"), "There")

    def test_remove_collision(self):
        self.ht.insert("Hello", "World")
        self.ht.insert("Hey", "There")

        self.assertTrue(self.ht.remove("Hello"))
        self.assertEqual(self.ht.contains("Hey"), "There")

    def test_update(self):
        pass
            
        
class test_edge_cases(unittest.TestCase):
    def setUp(self):
        self.ht = hash_table()

    def test_insert_duplicate(self):
        self.assertTrue(self.ht.insert("Hello", "World"))
        self.assertFalse(self.ht.insert("Hello", "World"))

    def test_remove_non_existent_key(self):
        self.assertFalse(self.ht.remove("Hello"))

    def test_remove_same_key_twice(self):
        self.ht.insert("Something","New")
        self.assertTrue(self.ht.remove("Something"))
        self.assertFalse(self.ht.remove("Something"))

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            hash_table(-10)

    def test_invalid_key(self):
        ht = hash_table()
        with self.assertRaises(TypeError):
            ht.insert(None, "value")

    def test_update(self):
        pass

if __name__ == "__main__":
    unittest.main()