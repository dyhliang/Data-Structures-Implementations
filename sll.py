# Description: This file contains various methods that modify or obtain info frm a linked list
#               (which utilizes a front sentinel node). 


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds a node at the beginning of the LL(after the right sentinel).

        param: value - an object for the LL

        return: None
        """

        # Utilizes a temp variable to point to new Node and changing the links
        curr = self._head
        temp = curr.next
        curr.next = SLNode(value)
        curr.next.next = temp

    def insert_back(self, value: object) -> None:
        """
        Adds a node at the back of the LL.

        param: value - an object for the LL

        return: None
        """

        # Sets curr to the front sentinel node
        # Loop until the end of LL, then jump out and set curr.next to a node with the argument value
        curr = self._head
        while curr.next is not None:
            curr = curr.next
        curr.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a node at the specified valid index of the LL.

        param: value - an object for the LL
               index - integer that is in the range [0, N] inclusive

        return: None
        """

        # Sets curr to the front sentinel node, position to 0
        curr = self._head
        pos = 0

        # Raises exception if index not in valid range
        if index not in range(0, self.length() + 1):
            raise SLLException

        # Iterate through until pos is the same as index, uses temp to swap the links
        while pos != index:
            curr = curr.next
            pos += 1
        temp = curr.next
        curr.next = SLNode(value)
        curr.next.next = temp

    def remove_at_index(self, index: int) -> None:
        """
        Removes a node at the specified valid index of the LL.

        param: index - an integer within the range of [0, N-1] inclusive

        return: None
        """

        # Sets curr to front sentinel node, position to 0
        curr = self._head
        pos = 0

        # Checks for valid index
        if index not in range(0, self.length()):
            raise SLLException

        # Iterate until pos is equal to index, use temp to help swap the links
        while pos != index:
            curr = curr.next
            pos += 1
        temp = curr.next.next
        curr.next = temp

    def remove(self, value: object) -> bool:
        """
        Removes the first node that matches the argument value

        param: value - a target object

        return: a boolean indicating whether removal was successful
        """

        # Sets curr to the node after the front sentinel, counter to 0
        curr = self._head.next
        pos = 0

        # Keeps iterating through the list until a match is found, calls on remove_at_index() to remove
        # Returns false if the LL is able to iterate to the end
        while curr is not None:
            if curr.value == value:
                self.remove_at_index(pos)
                return True
            else:
                curr = curr.next
                pos += 1

        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that matches the argument value

        param: value - a target object

        return: int - an integer counting occurrences of said value
        """

        # Sets curr to the node after the front sentinel, count to 0
        curr = self._head.next
        count = 0
        while curr is not None:
            if curr.value == value:
                count += 1
            curr = curr.next

        return count

    def find(self, value: object) -> bool:
        """
        Searches for a given value in the LL.

        param: value - a target object

        return: boolean indicating whether the value exists in the list.
        """

        # Sets curr to the node after the front sentinel 
        # iterates through the list until a match is found, otherwise return False
        curr = self._head.next
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Produces a new LL containing a certain number of nodes from the original LL

        param: start_index - an integer, must be within [0, N-1] range inclusively.
               size - a non-negative integer indicating the number of nodes requested from start_index

        return: a modified LL containing the requested values
        """

        # Validates start_index and size
        if start_index not in range(0, self.length()) or size < 0 or start_index + size > self.length():
            raise SLLException

        # Initializes a new LL, sets positiion to 0 and curr to the node after the front sentinel
        sliced_ll = LinkedList()
        pos = 0
        curr = self._head.next

        # Iterates through the LL while incrementing the position, if the position is within the
        # requested range, call on insert_back() to add the value at current node to new LL
        while curr is not None:
            if pos in range(start_index, start_index + size):
                sliced_ll.insert_back(curr.value)
            curr = curr.next
            pos += 1

        return sliced_ll


if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
