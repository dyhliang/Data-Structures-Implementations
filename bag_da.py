# Description: This class contains functions that can be used to modify the bag ADT.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds new element to Bag

        param: value - an object to be added

        return: None
        """

        # uses the append() method from DA class
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes any one element from bag that matches the argument value.

        param: value - the target element to remove

        return: boolean value indicating whether removal was successful
        """

        # iterates through bag to check for target item to remove
        for pos in range(self.size()):
            if self._da[pos] == value:
                self._da.remove_at_index(pos)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Counts number of elements in the bag that matches target value.

        param: value - the target element to count

        return: a counter of matching values
        """

        # iterates through bag to look for matching values and increment count if so
        count = 0
        for pos in range(self.size()):
            if self._da[pos] == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Clears the contents of the bag.

        param: None
        
        return: None
        """

        # References to a blank new DA
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Checks of contents of two bags are the same.

        param: second_bag - a Bag object

        return: boolean based on whether the bags are the same
        """

        # Bags don't match if they have different sizes.
        if self.size() != second_bag.size():
            return False
        
        # calls on count() to get the count for number at current index of first bag, we only need
        # the index in the first bag because we test with the assumption that the number at the current
        # index of the first bag exists in the second bag, if not, return False.
        for pos in range(self.size()):
            if self.count(self._da.get_at_index(pos)) != second_bag.count(self._da.get_at_index(pos)):
                return False
        
        return True

    def __iter__(self):
        """
        Enables bag to iterate across itself.

        return: self
        """

        self._index = 0

        return self

    def __next__(self):
        """
        Obtain next value and advance iterator

        return: the next value
        """

        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
