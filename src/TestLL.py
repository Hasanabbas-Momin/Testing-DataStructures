import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_back(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(3)

        self.assertFalse(linked_list.is_empty())
        self.assertEqual(linked_list.size, 3)

    def test_insert_front(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.insert_front(3)

        self.assertFalse(linked_list.is_empty())
        self.assertEqual(linked_list.size, 3)

    def test_insert_after(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(4)
        linked_list.insert_back(5)

        linked_list.insert_after(2, 3)

        self.assertEqual(linked_list.size, 5)
        self.assertEqual(linked_list.head.data, 1)

    def test_remove_first(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(3)

        self.assertEqual(linked_list.remove_first().data, 1)
        self.assertEqual(linked_list.size, 2)

    def test_update(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(3)

        # print("debugging1");
        self.assertEqual(linked_list.update(2, 4), 4)
        self.assertEqual(linked_list.size, 3)
        # print("debugging2");

    def test_remove_last(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(3)

        self.assertEqual(linked_list.remove_last(), 3)
        self.assertEqual(linked_list.size, 2)
        self.assertEqual(linked_list.remove_last(), 2)
        self.assertEqual(linked_list.size, 1)
        self.assertEqual(linked_list.remove_last(), 1)
        self.assertEqual(linked_list.size, 0)

    def test_remove(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert_back(1)
        linked_list.insert_back(2)
        linked_list.insert_back(3)

        self.assertEqual(linked_list.remove(2), 2)
        self.assertEqual(linked_list.size, 2)
        self.assertEqual(linked_list.remove(1), 1)
        self.assertEqual(linked_list.size, 1)

    def test_exceptions(self):
        linked_list = LinkedList()

        with self.assertRaises(RuntimeError):
            linked_list.remove_first()

        with self.assertRaises(RuntimeError):
            linked_list.remove_last()

        with self.assertRaises(RuntimeError):
            linked_list.remove(1)

if __name__ == '__main__':
    unittest.main()
