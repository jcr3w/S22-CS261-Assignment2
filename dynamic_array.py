# Name: Justin Greer
# OSU Email: greerjus@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 - Dynamic Array
# Due Date: April 25, 2022
# Description:


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
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Method that changes the capacity of the underlying storage.
        """

        new_data = [None] * new_capacity

        # Method only accepts positive integers for new_capacity and new_capacity cannot be smaller than the
        # elements currently stored in the dynamic array.  If false, end program and return nothing.
        if new_capacity <= 0 or new_capacity < self._size:
            return

        if new_capacity <= 0 or new_capacity < self._size:
            return

        # Create new data elements to be used in updated array elements
        for num in range(self._size):
            new_data[num] = self._data[num]

        # Updates capacity and data to new_capacity and new_data, respectuflly.
        self._capacity = new_capacity
        self._data = new_data

    def append(self, value: object) -> None:
        """
        Method that enables user to add new value to the end of a dynamic array.
        """

        # Check to see if the size if size is greater than capacity.  If true, double the capacity
        # before adding a new value.
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)

        # TBD.  Rewrite in cleanup.
        self._data[self._size] = value
        self._size = self._size + 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method that adds new value at a specific location in the array (index).
        """

        # If the provided index is invalid, the method raises a custom
        # “DynamicArrayException”
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # Check to see if the size if size is greater than capacity.  If true, double the capacity
        # before adding a new value.
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)

        # Range(start, stop, and increment)
        for num in range(self._size, index, -1):
            less_num = num - 1
            self._data[num] = self._data[less_num]

        # Update value at the correct index
        self._data[index] = value

        # increase the size (number of elements in the array).  If size exceeds capacity, double capacity (see above).
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """

        if index < 0 or index > self._size:
            raise DynamicArrayException

        # When the number of elements stored in the array (before removal) is STRICTLY LESS than
        # ¼ of its current capacity, the capacity must be reduced to TWICE the number of current
        # elements. This check / capacity adjustment must happen BEFORE removal of the element.

        # If the current capacity (before reduction) is 10 elements or less, reduction should not occur
        # at all. If the current capacity (before reduction) is greater than 10 elements, the reduced
        # capacity cannot become less than 10 elements. Please see the examples below, especially
        # example #3, for clarification.

        if (self._size * 2) < 10 and self._size < (self._capacity / 4):
            self.resize(10)
        elif (self._size * 2) >= 10 and self._size < (self._capacity / 4):
            self.resize(self._size * 2)

        for num in range(index, self._size -1, 1):
            self._data[num] = self._data[num+1]

        self._data[self._size - 1] = None

        # increase the size (number of elements in the array).  If size exceeds capacity, double capacity (see above).
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        TODO: Write this implementation
        """

        start = start_index
        end = start_index + size

        if start < 0 or size < 0 or start >= (self._size) or self._size < end:
            raise DynamicArrayException

        input = (self._data[num] for num in range(start, end, 1))

        return DynamicArray(input)

    def merge(self, second_da: "DynamicArray") -> None:
        """
        TODO: Write this implementation
        """
        # This method takes another Dynamic Array object as a parameter, and appends all elements
        # from this other array onto the current one, in the same order as they are stored in the array
        # parameter.

        for num in range(second_da._size):
            self.append(second_da[num])

    def map(self, map_func) -> "DynamicArray":
        """
        TODO: Write this implementation
        """
        # This method creates a new Dynamic Array where the value of each element is derived by
        # applying a given map_func to the corresponding value from the original array.
        # This method works similarly to the Python map() function. For a review on how Python’s
        # map() works, here is some suggested reading

        new_arr = DynamicArray([])

        for num in range(DynamicArray.length(self)):
            new_arr.append(map_func(self[num]))
        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        TODO: Write this implementation
        """

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TODO: Write this implementation
        """
        pass


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    """
# Write a standalone function outside of the Dynamic Array class that receives a
# DynamicArray that is sorted in order, either non-descending or non-ascending. The function
# will return a tuple containing (in this order) a DynamicArray comprising the mode
# (most-occurring) value/s in the array, and an integer that represents the highest frequency
# (how many times they appear).
# If there is more than one value that has the highest frequency, all values at that frequency
# should be included in the array being returned, in the order in which they appear in the
# array parameter. If there is only one mode, return a DynamicArray comprised of only that
# value.
# You may assume that the input array will contain at least one element, and that values
# stored in the array are all of the same type (either all numbers, or strings, or custom
# objects, but never a mix of these). You do not need to write checks for these conditions.
# For full credit, the function must be implemented with O(N) complexity with no additional
# data structures (beyond the array you return) being created.


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
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
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
