import unittest
from Queue import ArrayQueue, LLQueue

class TestArrayQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = ArrayQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size, 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size, 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        self.assertEqual(queue.size, 1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), 3)

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size, 0)

    def test_peek(self):
        queue = ArrayQueue()
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(15)

        self.assertEqual(queue.peek(), 5)
        self.assertEqual(queue.size, 3)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size, 0)

        queue.enqueue(20)
        self.assertEqual(queue.peek(), 20)



    def test_exceptions(self):
        queue = ArrayQueue()

        with self.assertRaises(IndexError):
            queue.dequeue()

        with self.assertRaises(RuntimeError):
            queue.peek()

class TestLLQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = LLQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size, 0)

        # print(f"Initial size: {queue.size}")

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # print(f"Final size: {queue.size}")


        # self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size, 3)
        self.assertEqual(queue.dequeue().data, 1)
        self.assertEqual(queue.dequeue().data, 2)

        self.assertEqual(queue.size, 1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue().data, 3)

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size, 0)



    def test_exceptions(self):
        queue = LLQueue()

        with self.assertRaises(RuntimeError):
            queue.dequeue()

if __name__ == '__main__':
    unittest.main()
