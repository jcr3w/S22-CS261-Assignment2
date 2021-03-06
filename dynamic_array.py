# Name: Justin Greer
# OSU Email: greerjus@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 - Dynamic Array
# Due Date: April 25, 2022
# Description: Program that creates a number of methods for modifying, testing, and evaluating Dynamic Arrays.

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
        if new_capacity <= 0 or new_capacity < self.length():
            return

        if new_capacity <= 0 or new_capacity < self.length():
            return

        # Create new data elements to be used in updated array elements
        for num in range(self.length()):
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

        if self.length() >= self.get_capacity():
            self.resize(self.get_capacity() * 2)

        self._data[self.length()] = value
        self._size = self._size + 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method that adds new value at a specific location in the array (index).
        """

        # If the provided index is invalid, the method raises a custom
        # ???DynamicArrayException???
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # Check to see if the size if size is greater than capacity.  If true, double the capacity
        # before adding a new value.
        if self.length() >= self.get_capacity():
            self.resize(self.get_capacity() * 2)

        # Range(start, stop, and increment)
        for num in range(self.length(), index, -1):
            less_num = num - 1
            self._data[num] = self._data[less_num]

        # Update value at the correct index
        self._data[index] = value

        # increase the size (number of elements in the array).  If size exceeds capacity, double capacity (see above).
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Method that removes the element at the specified index in the dynamic array.
        """

        # Check for a DynamicArrayException
        if index < 0 or index > self.length() - 1:
            raise DynamicArrayException

        # Resize array based on rulers laid out in instructions.  Pre-Reduction Rules:
        # 1. If the number of elements is less than 1/4 of capacity, reduce capacity to twice the number of elements.
        # 2. If pre-reduction capacity is greater than 10, post-reduction capacity cannot be less than 10.
        # 3. If capacity is less than 10 elements, reduction shouldn't occur
        if self.get_capacity() > 10 and self.length() < self.get_capacity() / 4:
            if self.length() <= 4:
                self.resize(10)
            else:
                self.resize(self._size * 2)

        # The following loop and statements work through the array and remove the element at the specified index.

        for num in range(index, self.length() - 1, 1):
            self._data[num] = self._data[num + 1]

        self._data[self.length() - 1] = None

        # Decrease the size (number of elements in the array).  If size exceeds capacity, double capacity (see above).
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Method that takes the inputs 'start_index' and 'size' and returns a slice of elements that fall within
        the specified range.  For example, if an array of [1,2,3,4,5] is given and the start_index is 0 and the
        size is 3, the method will return [1,2,3].
        """

        # Define start of the slice and end of the slice
        start = start_index
        end = start_index + size

        # Define the criteria for a DynamicArrayException
        if start < 0 or size < 0 or start >= (self.length()) or self.length() < end:
            raise DynamicArrayException

        # Loop that iterates through the array starting at 'start', ending at 'end'
        input = (self._data[num] for num in range(start, end))

        return DynamicArray(input)

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Method that appends elements from one array to another
        """
        # This method takes another Dynamic Array object as a parameter, and appends all elements
        # from this other array onto the current one, in the same order as they are stored in the array
        # parameter.

        # Loop that uses the append method (as defined above) to append 'second_da' to the DynamicArray
        for num in range(second_da.length()):
            self.append(second_da[num])

    def map(self, map_func) -> "DynamicArray":
        """
        Method that creates a new Dynamic Array (new_arr) where each value is derived by applying the
        map_func to each value in the corresponding array.
        """

        # Create new DynamicArray called new_arr.  I think this took me over an hour to figure out that
        # I needed to put a [] inside the ().  -_-
        new_arr = DynamicArray([])

        # Loop through DynamicArray, derive the new values (apply map_func to each value in DynamicArray) and then
        # write the new findings to the new Dynamics Array (new_arr).  Return new_arr.
        for num in range(DynamicArray.length(self)):
            new_arr.append(map_func(self[num]))
        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        Method that creates a new Dynamic Array (new_arr) and only populates it with elements from the original
        array that the filter_func defines as TRUE.
        """

        # Create new DynamicArray called new_arr.  Learned my lesson from the map method.
        new_arr = DynamicArray([])

        # Loop through DynamicArray, write the values from the original array to 'new_arr' that are deemed true
        # by filter_func.  Return new_arr.
        for num in range(DynamicArray.length(self)):
            if filter_func(self[num]) == True:
                new_arr.append(self[num])
        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Method that sequentially applies the reduce_func to all elements of the Dynamic Array, and
        returns the resulting value.
        """

        # Create new array to hold outputs
        new_arr = DynamicArray([])
        value = self[0]

        # Loop through array, set initializer
        for num in range(self.length()):
            if initializer is None:
                value = self[0]
            else:
                value = initializer

        # Loop through array, sequentially apply the reduce_func.  Return value.
        for num in range(self.length()):
            if initializer is None:
                value = value
            new_arr.append(reduce_func(value, self[num]))
            value = reduce_func(value, self[num])
        return value

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Write a method that returns the mode and the frequency.
    """

    mode = DynamicArray([])
    frequency = DynamicArray([])
    counter = 1

    while counter < arr.length():
        if arr[counter] == arr[counter - 1]:
            mode.append(arr[counter])
            frequency = counter
        counter += 1

    return mode, frequency


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
