# Description: This class contains functions that can be used to modify the dynamic array ADT.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(
            f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes capacity of the dynamic array.

        param: new_capacity - a positive integer that should be greater than or equal to
                            the current size of the array.

        returns: None
        """

        # Checks that the new capacity is valid
        if new_capacity < 1 or new_capacity < self._size:
            return

        # Sets the new capacity
        self._capacity += (new_capacity - self._capacity)
        new_arr = StaticArray(new_capacity)

        # Copies old array to new resized array
        for pos in range(self._size):
            new_arr[pos] = self._data[pos]

        # References self._data back to the new array
        self._data = new_arr

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array.

        param: value - an object that will be appended to the dynamic array.

        returns: None
        """

        # If the storage is full, double the capacity, then perform the append and update _size.
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index in the DA.

        param: index - an integer position to insert the new object
               value - an object that is inserted at the index above

        return: None
        """

        # Doubles the capacity if the storage is full
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Raises an exception if the index is not in the valid range
        if index not in range(0, self._size + 1):
            raise DynamicArrayException

        # Shifts the values at the indices after the insertion forward
        for pos in range(self._size, index, -1):
            self._data[pos] = self._data[pos - 1]

        # Performs the insertion, updates size of array
        self._size += 1
        self._data[index] = value

    def remove_at_index(self, index: int) -> None:
        """
        Remove a new value at the specified index in the DA.

        param: index - an integer position to remove the new object

        return: None
        """

        # Raises an exception if the index is not in the valid range
        if index not in range(0, self._size):
            raise DynamicArrayException

        # Capacity reduction conditions
        if (self._size < self._capacity * .25) and (self._capacity > 10):
            if self._size * 2 < 10:
                self._capacity = 10
            else:
                self._capacity = self._size * 2

        # Shifts the values at the indices after the removal back, then updates the size
        for pos in range(index, self._data.length() - 1):
            self._data[pos] = self._data[pos + 1]

        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Produces the requested number of elements at the indices given

        param: start_index - integer for the lowerbound of the index range
               size - the amount of requested elements from the array from the starting index

        return: a DynamicArray containing numbers from the aforementioned range
        """

        # Checks to see that the index is in range [0, N-1] inclusive, size is a non-negative integer
        # and that the requested range does not fall outside the array.
        if start_index not in range(0, self._size) or size < 0 or start_index + size > self._size:
            raise DynamicArrayException

        # Creates new DA to store the requested range of numbers
        new_arr = DynamicArray()
        for start_index in range(start_index, start_index + size):
            new_arr.append(self._data[start_index])

        return new_arr

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Appends argument array to the current array.

        param: second_da - the array to be appended to the current array

        return: None
        """

        # Calls append() to append each element of the second DA
        for pos in range(second_da.length()):
            self.append(second_da[pos])

    def map(self, map_func) -> "DynamicArray":
        """
        Produces new DA where each value is derived from a given function to the corresponding
        values from the original array.

        param: map_func - an anonymous function with its own set of parameters

        return: a DynamicArray with the modified values from the mapped functions
        """

        # Creates new_arr and calls on map_func to modify values
        new_arr = DynamicArray()
        for pos in range(self._size):
            new_arr.append(map_func(self._data[pos]))

        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        Produces new DA with only elements from original array for which filter_func returns true.

        param: filter_func - a boolean function

        return: a modified DA with elements for which filter_func returns True
        """

        # Creates new_arr and calls on filter_func to validate values
        new_arr = DynamicArray()
        for pos in range(self._size):
            if filter_func(self._data[pos]):
                new_arr.append(self._data[pos])

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies reduce_func to all elements in DA

        param: reduce_func - an anonymous function with its own set of parameters
               initializer - an integer, otherwise a default argument

        return: an object that is the result of the reduce function
             or initializer if the DA is empty
             or None if neither is provided
        """

        # Checks to see if the DA is empty before iterating through elements ot apply reduce_func
        if self._size == 0:
            return initializer

        # The starting index for iteration will be 0 or 1 based on whether an initializer is given.
        # Likewise, result will start off with the value at index 0 or the initializer.
        if initializer is None:
            result = self.get_at_index(0)
            start_pos = 1
        else:
            result = initializer
            start_pos = 0

        for pos in range(start_pos, self._size):
            result = reduce_func(result, self.get_at_index(pos))

        return result

    def pop(self) -> int:
        """
        Removes the last item in a DA and updates size count

        @Param: None
        @Return: the integer at the last index
        """
        pop_last = self._data[self._size - 1]
        self._size -= 1
        return pop_last


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Finds the mode and frequency of such value in a non-descending/ascending DynamicArray.

    param: arr - a sorted DynamicArray that is non-descending/ascending

    return: a tuple - (DynamicArra of the mode value(s),
                    integer representing highest frequency of modul value(s))
    """

    # Stores all unique values in original array
    unique_vals = DynamicArray()
    unique_vals.append(arr[0])
    for pos in range(1, arr.length()):
        if arr[pos] != arr[pos - 1]:
            unique_vals.append(arr[pos])

    # Creates an occurrence array with same size as unique_vals, filling it with 0s to increment.
    occ_arr = DynamicArray()
    for pos in range(0, unique_vals.length()):
        occ_arr.append(0)

    # Iterates through original array and unique values array to update occurrences array based on matches.
    # The indices for occurences and unique values are corresponding.
    unique_pos = 0
    for pos in range(arr.length()):
        if arr[pos] == unique_vals[unique_pos]:
            occ_arr[unique_pos] += 1
        else:
            unique_pos += 1
            if occ_arr[unique_pos] == 0:
                occ_arr[unique_pos] += 1

    # Creates mode array to store unique values that are modes
    # Uses standard algorithm to find the max of the occurrences array's values
    # Uses >= instead of > because we want to find modes with same frequency value, not just the first
    mode_arr = DynamicArray()
    max_freq = occ_arr[0]
    for pos in range(occ_arr.length()):
        if occ_arr[pos] >= max_freq:
            max_freq = occ_arr[pos]

    # Iterates through occurrences array once more after max_freq is finalized, the value in unique values
    # that corresponds to the max frequency amount(s) in the occurences array will be appended to the mode array.
    for pos in range(occ_arr.length()):
        if occ_arr[pos] == max_freq:
            mode_arr.append(unique_vals[pos])

    return mode_arr, max_freq


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ",
              da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")

    print("\n# pop - example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"DYN_ARR before: {da}")
    print(f"Popped value: {da.pop()}")
    print(f"DYN_ARR after: {da}")
