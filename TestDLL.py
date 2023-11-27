import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_is_empty(self):
        dll = DoublyLinkedList()
        self.assertTrue(dll.is_empty())

        dll.insert_front(1)
        self.assertFalse(dll.is_empty())

        dll.remove_back()
        self.assertTrue(dll.is_empty())

    def test_insert_front(self):
        dll = DoublyLinkedList()
        dll.insert_front(1)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 1)

        dll.insert_front(2)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.data, 2)
        self.assertEqual(dll.tail.data, 1)

    def test_insert_back(self):
        dll = DoublyLinkedList()
        dll.insert_back(1)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 1)

        dll.insert_back(2)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 2)

    def test_remove_front(self):
        dll = DoublyLinkedList()
        dll.insert_front(1)
        dll.insert_front(2)

        data = dll.remove_front()
        self.assertEqual(data, 2)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 1)

    def test_remove_back(self):
        dll = DoublyLinkedList()
        dll.insert_back(1)
        dll.insert_back(2)

        data = dll.remove_back()
        self.assertEqual(data, 2)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 1)

    def test_insert_after(self):
        dll = DoublyLinkedList()
        dll.insert_back(1)
        dll.insert_back(3)

        dll.insert_after(1, 2)
        self.assertEqual(dll.size, 3)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 3)

        dll.insert_after(1, 4)
        self.assertEqual(dll.size, 4)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 3)

    def test_remove(self):
        dll = DoublyLinkedList()
        dll.insert_back(1)
        dll.insert_back(2)
        dll.insert_back(3)

        dll.remove(2)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.tail.data, 3)

        dll.remove(1)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.data, 3)
        self.assertEqual(dll.tail.data, 3)

    def test_display(self):
        dll = DoublyLinkedList()
        dll.insert_back(1)
        dll.insert_back(2)
        dll.insert_back(3)

        self.assertEqual(dll.display(), [1, 2, 3])

# Add more test cases following the suggestions above.


if __name__ == '__main__':
    unittest.main()
