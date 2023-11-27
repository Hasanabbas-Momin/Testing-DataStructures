import unittest
from stack import *

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size, 0)

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size, 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)

        self.assertEqual(stack.size, 1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 1)

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size, 0)

    def test_peek(self):
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.push(15)

        self.assertEqual(stack.peek(), 15)
        self.assertEqual(stack.size, 3)

    def test_exceptions(self):
        stack = Stack()

        with self.assertRaises(RuntimeError):
            stack.pop()

        with self.assertRaises(RuntimeError):
            stack.peek()

if __name__ == '__main__':
    unittest.main()
