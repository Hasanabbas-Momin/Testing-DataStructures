import unittest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

    def test_insert_and_inorder_traversal(self):
        expected_result = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(self.bst.inorder_traversal(), expected_result)

    def test_delete_leaf_node(self):
        self.bst.delete(20)
        expected_result = [30, 40, 50, 60, 70, 80]
        self.assertEqual(self.bst.inorder_traversal(), expected_result)
        self.bst.delete(30)
        expected_result = [ 40, 50, 60, 70, 80]

    def test_delete_node_with_one_child(self):
        self.bst.delete(30)
        expected_result = [20, 40, 50, 60, 70, 80]
        self.assertEqual(self.bst.inorder_traversal(), expected_result)

    def test_delete_node_with_two_children(self):
        self.bst.delete(50)
        expected_result = [20, 30, 40, 60, 70, 80]
        self.assertEqual(self.bst.inorder_traversal(), expected_result)



if __name__ == '__main__':
    unittest.main()
