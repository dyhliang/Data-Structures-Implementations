# Description: Implements various methods to manipulate/access a DA that is built as a MinHeap


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds new object to the MinHeap while maintaining heap property.

        @param: node - the object to be added
        @return: None
        """
        # Special case for when the heap is empty to avoid negative parent_pos value
        if self._heap.length() == 0:
            self._heap.append(node)
        else:
            pos = self._heap.length()
            parent_pos = int((pos - 1) // 2)
            self._heap.append(node)
            # Halves the DA every iteration for O(log n) complexity
            while self._heap[pos] < self._heap[parent_pos]:
                self.swap(pos, parent_pos)
                pos = parent_pos
                if pos > 0:
                    parent_pos = int((pos - 1) // 2)

    def swap(self, pos_1, pos_2) -> None:
        """
        Helper function to perform the swap utilizing a tuple

        @param: pos_1 - index of the first element to be swapped
                pos_2 - index of the second element to be swapped
        @return: None
        """
        self._heap[pos_1], self._heap[pos_2] = self._heap[pos_2], self._heap[pos_1]

    def is_empty(self) -> bool:
        """
        Determines whether the heap is empty or not

        @param: None
        @return: a boolean indicating whether a heap has a length of 0
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Finds the minimum value in a heap.

        @param: None
        @return: integer value at heap[0]
        """
        if self._heap.is_empty():
            raise MinHeapException

        return self._heap[0]

    def remove_min(self) -> object:
        """
        Removes the minimum value from a heap.

        @param: None
        @return: The minimum value object that was removed
        """
        # Validates whether heap is empty
        if self._heap.is_empty():
            raise MinHeapException

        # Stores min value, pops the heap and percolates down to maintain heap property
        min_val = self.get_min()
        popped_val = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = popped_val
            _percolate_down(self._heap, 0)
        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a min heap using a DA of objects, overwrites current contents of MinHeap.
        Runs on O(N) time complexity.

        @param: da - a Dynamic Array
        @return: None
        """
        # initializes a new heap, then copies the contents over before percolating.
        new_heap = DynamicArray()
        for pos in range(da.length()):
            new_heap.append(da[pos])
        self._heap = new_heap

        # Start at the first non leaf node, moving backwards and percolating down for each subtree of the node
        non_leaf = int(da.length() // 2 - 1)
        while non_leaf >= 0:
            _percolate_down(self._heap, non_leaf)
            non_leaf -= 1

    def size(self) -> int:
        """
        Returns the length of the heap.

        @param: None
        @return: an integer indicating the length of the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        References heap to a blank Dynamic Array.

        @param: None
        @return: None
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Performs heapsort on a DA with the help of percolate_down to build a MinHeap first.

    @param: da - a Dynamic Array of objects
    @return: None
    """

    # initializes non_leaf as the index for the first non_leaf node, then using it with percolate down to set up the
    # MinHeap
    non_leaf = int(da.length() // 2 - 1)
    while non_leaf >= 0:
        _percolate_down(da, non_leaf)
        non_leaf -= 1

    # k is the sorted portion that is kept apart from the rest
    k = da.length() - 1
    while k >= 0:
        pos = 0
        left = 2 * pos + 1
        right = 2 * pos + 2

        # if statement makes sure that the swap only happens when the root node is less than the kth value, had some
        # edge cases where the root and its left child didn't move correctly
        if da[k] >= da[pos]:
            da[0], da[k] = da[k], da[0]
        k -= 1

        # Iterates as long as the left child is not in the k region
        # Checks to make sure that it percolates to left child only if left <= right AND the current value is >
        # than the left child.
        while left <= k:
            if da[left] <= da[right] and da[pos] > da[left]:
                da[pos], da[left] = da[left], da[pos]
                pos = left
            else:
                # When the right child is in the k section, switch with the left instead
                # Otherwise, make sure the current value is > right child before swapping
                if right > k:
                    da[pos], da[left] = da[left], da[pos]
                elif da[pos] > da[right]:
                    da[pos], da[right] = da[right], da[pos]
                pos = right

            left = 2 * pos + 1
            right = 2 * pos + 2


def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Helper function that moves an element down to the last row of the heap to establish/maintain MinHeap property.

    @param: da - the DynamicArray ADT used to store the elements
            parent - the integer index of an object
    @returns: None
    """
    pos = parent
    left = 2 * pos + 1
    right = 2 * pos + 2

    # left index has to be within the length of the DA but not equal to
    # right index check - can be == da's length, in that case swap with left child
    # otherwise, as long as the current value is > than its left or right children
    # -swap with the left if left <= right
    # -swap with the right if otherwise
    while left < da.length():
        if right >= da.length():
            if da[pos] > da[left]:
                da[pos], da[left] = da[left], da[pos]
            return
        elif da[pos] >= da[left] or da[pos] >= da[right]:
            if da[left] <= da[right]:
                da[pos], da[left] = da[left], da[pos]
                pos = left
            else:
                da[pos], da[right] = da[right], da[pos]
                pos = right
        else:
            # If I'm being honest, I don't know what case this return covers exactly, I tried this out on a whim, and it
            # helped me break out of an infinite loop quite a few times - I think it's just a catch-all for scenarios
            # where the current value is already < than its children, so it doesn't need to percolate further?
            return

        left = 2 * pos + 1
        right = 2 * pos + 2


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 3")
    print("--------------------------")
    da = DynamicArray([53, 29, 34, 32, 44, 11, 21, 18, 66, 25, 15, 20])
    h = MinHeap([-30393, 27217, 44458, 65619])
    print(h)
    h.build_heap(da)
    print(h)

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 6")
    print("------------------------")
    da = DynamicArray([91722, 3387, -373, -32385, 11199, 28850, -31611, 77027, 83254, 74304])
    print(f"Before: {da}")
    print("Expected: DYN_ARR Size/Cap: 10/16 [91722, 83254, 77027, 74304, 28850, 11199, 3387, -373, -31611, -32385]")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 5")
    print("------------------------")
    da = DynamicArray([-44497, -69146, 52579, 7806, 69689, -30920, 42625, 90198, -82180])
    print(f"Before: {da}")
    print("Expected: DYN_ARR Size/Cap: 9/16 [90198, 69689, 52579, 42625, 7806, -30920, -44497, -69146, -82180]")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 4")
    print("------------------------")
    da = DynamicArray([31655, 95698, -69168, 79718, -71170, 951, 25671])
    print(f"Before: {da}")
    print("Expected: DYN_ARR Size/Cap: 7/8 [95698, 79718, 31655, 25671, 951, -69168, -71170]")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 3")
    print("------------------------")
    da = DynamicArray([32, 12, 2, 8, 16, 20, 24, 40, 4])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
