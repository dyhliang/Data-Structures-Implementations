# Description: Implements the Queue ADT with a static array.


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue.

        param: value - object to be enqueued

        return: None
        """
        # If the queue's current size is the same as the initialized size, call on double queue
        # to double the capacity
        if self._sa.length() == self.size():
            self._double_queue()

        # Otherwise increment the back index, enqueue and increment size of queue
        self._back = self._increment(self._back)
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """
        Remove and returns the value at the beginning of the queue.

        param: None

        return: the object at the beginning of the queue
        """
        # Checks if the queue is empty
        if self.is_empty():
            raise QueueException

        # Stores dequeue value before incrementing the front index, then decrements size of current queue
        dequeue_val = self._sa[self._front]
        self._front = self._increment(self._front)
        self._current_size -= 1
        return dequeue_val

    def front(self) -> object:
        """
        Returns the front element of the queue without removing it.

        param: None

        return: object representing the front element of queue
        """
        # Checks if queue is empty, otherwise return the value at the front index
        if self.is_empty():
            raise QueueException
        return self._sa[self._front]

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        Helper method for enqueue() to double size of queue 

        param: None

        return: None
        """
        # Initializes new array with double the capacity, then iterate to copy original queue to new
        # queue before referencing self_sa to the new queue.
        new_sa = StaticArray(2 * self._current_size)
        for pos in range(self._sa.length()):
            new_sa[pos] = self._sa[pos]

        self._sa = new_sa

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
