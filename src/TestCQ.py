import unittest
from circular_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        cq = CircularQueue(5)
        self.assertTrue(cq.is_empty())
        self.assertFalse(cq.is_full())

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.enqueue(4)


        self.assertFalse(cq.is_empty())
        self.assertFalse(cq.is_full())
        self.assertEqual(cq.size, 4)

        self.assertEqual(cq.dequeue(), 1)
        self.assertEqual(cq.dequeue(), 2)
        self.assertEqual(cq.size, 2)

        cq.enqueue(5)
        cq.enqueue(6)
        cq.enqueue(7)


        self.assertEqual(cq.size, 5)



        self.assertFalse(cq.is_empty())
        self.assertTrue(cq.is_full())
        self.assertEqual(cq.size, 5)

        self.assertEqual(cq.dequeue(), 3)
        self.assertEqual(cq.dequeue(), 4)

        self.assertEqual(cq.size, 3)
        self.assertFalse(cq.is_empty())
        self.assertFalse(cq.is_full())

    def test_display(self):
        cq = CircularQueue(5)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.enqueue(4)

        self.assertEqual(cq.display(), [1, 2, 3, 4])

        cq.dequeue()
        cq.dequeue()
        cq.dequeue()

        self.assertEqual(cq.display(), [4])

        cq.enqueue(5)
        cq.enqueue(6)
        cq.enqueue(7)

        self.assertEqual(cq.display(), [4, 5, 6, 7])

    def test_exception_handling(self):
        cq = CircularQueue(3)

        with self.assertRaises(RuntimeError):
            cq.dequeue()

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)

        with self.assertRaises(RuntimeError):
            cq.enqueue(4)

        cq.dequeue()
        cq.dequeue()
        cq.dequeue()

        with self.assertRaises(RuntimeError):
            cq.dequeue()

if __name__ == '__main__':
    unittest.main()
