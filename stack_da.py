# Description: Implements a Stack ADT with various methods using Dynamic Arrays.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element on top of the stack using append()

        param: value - an object to be pushed

        return: None
        """
        self._da.append(value)

    def pop(self) -> object:
        """
        Removes element on the top of the stack

        param: value - an object to be popped

        return: the value that was popped, or a StackException error if the stack is empty.
        """

        # Checks if the stack has a size of 0
        if self.is_empty():
            raise StackException

        # Stores last index and its value before it is popped
        last_index = self.size() - 1
        popped_val = self._da.get_at_index(last_index)
        self._da.remove_at_index(last_index)
        return popped_val

    def top(self) -> object:
        """
        Returns the value at the top of the stack

        param: None

        return: the object at the top of the stack, or StackException if stack is empty
        """

        # Checks if the stack has a size of 0, if not, returns the value at the last index
        if self.is_empty():
            raise StackException
        last_index = self.size() - 1
        return self._da.get_at_index(last_index)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
