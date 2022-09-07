# Description: A BST with various methods to manipulate and obtain information
#               from within.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new node to tree while maintaining its BST property.

        param: value - a BSTNode object
        return: None
        """

        # Checks for whether the BST is empty before adding to a leaf node
        # Iterating left/right based on whether target value is less/greater than
        # or equal to the target value
        new_node = BSTNode(value)
        if self._root is None:
            self._root = new_node
        else:
            curr = self._root
            while curr is not None:
                if value >= curr.value:
                    if curr.right is None:
                        curr.right = new_node
                        return
                    curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = new_node
                        return
                    curr = curr.left

    def remove(self, value: object) -> bool:
        """
        Removes a node from the tree

        param: value - a BSTNode object
        return: boolean indicating whether removal was successful
        """
        # Initialize prev and curr to be parent and current node respectively.
        prev = None
        curr = self._root

        # Keep iterating left/right when there isn't a match
        while (curr is not None) and (curr.value != value):
            prev = curr
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left

        # If there is a match, curr will be the node that will be removed, 
        # return False if there wasn't a match
        if curr is None:
            return False

        # calls on helper methods below to reduce clutter in this method
        if curr.left == curr.right == None:
            self._remove_no_subtrees(prev, curr)
        elif curr.left is not None and curr.right is not None:
            self._remove_two_subtrees(prev, curr)
        else:
            self._remove_one_subtree(prev, curr)

        return True

    def _remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Handles removal of leaf nodes.

        param: the parent and current BST nodes
        return: None
        """
        # remove node that has no subtrees (no left or right nodes)

        # Base case, a BST with just a root has no subtrees
        # Otherwise set the node to the parent's left/right to None
        if parent is None:
            self._root = None
        else:
            if node == parent.left:
                parent.left = None

            if node == parent.right:
                parent.right = None

    def _remove_one_subtree(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Handles removal of nodes with one subtree.

        param: the parent and current BST nodes
        return: None
        """

        # store reference of node's left or right into temp so that we can
        # refer to it when rearranging
        temp = None
        if node.left is None:
            temp = node.right
        else:
            temp = node.left

        # Checks for cases where the parent node exists for current node or 
        # if current node is the root.
        if parent is not None:
            if node == parent.left:
                parent.left = temp
            else:
                parent.right = temp
        else:
            if node.left is None:
                self._root = node.right
            else:
                self._root = node.left

        node = None

    def _remove_two_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Handles removal of nodes with 2 subtrees.

        param: the parent and current BST nodes
        return: None
        """

        # initialize s to be inorder_successor, ps to be parent to s
        s = node.right
        ps = parent

        # keep going left until we can't for the inorder successor
        while s.left is not None:
            ps = s
            s = s.left

        # If successor is on the node's left, change the parent's left to the
        # successor's right, the current node's value is replaced with successor's value
        # If successor is on the node's right, change the current node's value to the 
        # successor's value, and then make the current node's right to point to successor's 
        # right. Reset successor value to None when done to avoid the extra branch.
        if s != node.right:
            ps.left = s.right
            node.value = s.value
        else:
            node.value = s.value
            node.right = s.right

        s = None

    def contains(self, value: object) -> bool:
        """
        Checks if the BST contains a node with the target value

        param: value - a target value
        return: boolean - indicating whether the value was found
        """

        # False by default if BST is empty
        if self.is_empty():
            return False

        # Keep iterating left/right based on whether target value is greater than
        # or less than or equal to the node value
        curr = self._root
        while curr is not None:
            if curr.value == value:
                return True

            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left

        return False

    def inorder_traversal(self) -> Queue:
        """
        Performs an inroder traversal of the BST.

        param: None
        return: Queue object containing values of visited nodes in the order visited
                If the tree is empty, an empty Queue is returned
        """

        if self.is_empty():
            return Queue()

        # Initializes a result queue containing the final order of values
        # Helper stack to help store the values when traversing
        curr = self._root
        result_queue = Queue()
        helper_stack = Stack()

        # When iterating: going down levels is push, going up is pop, applies a depth first search approach. Keep
        # going left until the leftmost node is reached, then pop to go down the node with a right subtree. Once all
        # the nodes from the left subtree is exhausted, go back up to the root. The root is popped from the stack and
        # added to the queue when we've gotten to the rightmost child of the left subtree. Then go to the right
        # subtree and apply a similar process. While loop has 2 conditions, the helper_stack being non-empty helps to
        # keep the loop going by going to the else portion after we've reached our leftmost leaf which would trigger
        # a curr is None situation.
        while not (helper_stack.is_empty()) or (curr is not None):
            if curr is not None:
                helper_stack.push(curr)
                curr = curr.left
            else:
                curr = helper_stack.pop()
                result_queue.enqueue(curr.value)
                curr = curr.right

        return result_queue

    def find_min(self) -> object:
        """
        Finds the node with the minimum value

        param: None
        return: BSTNode value that is the minimum
        """

        # No min if BST is empty
        if self.is_empty():
            return None

        # Min is found in the leftmost leaf
        curr = self._root
        while curr.left is not None:
            curr = curr.left

        return curr.value

    def find_max(self) -> object:
        """
        Finds the node with the maximum value

        param: None
        return: BSTNode value that is the maximum
        """

        # No max if BST is empty
        if self.is_empty():
            return None

        # Max is found in the rightmost leaf
        curr = self._root
        while curr.right is not None:
            curr = curr.right

        return curr.value

    def is_empty(self) -> bool:
        """
        Checks if the BST is empty

        param: None
        return: boolean indicating whether the root is None
        """
        return self._root is None

    def make_empty(self) -> None:
        """
        Clears out a BST - deforestation that is not harmful to the environment

        param: None
        return: None
        """

        # if the BST is not empty, 'snip' the branches leading to the two subtrees
        # from the root, then make the root None
        if not self.is_empty():
            self._root.left = None
            self._root.right = None
            self._root = None


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (44, 57, 32, 38, 54, 51),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
