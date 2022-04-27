# Name: Justin Greer
# OSU Email: greerjus@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 - Dynamic Array
# Due Date: April 25, 2022
# Description: Program that creates a number of methods for modifying, testing, and evaluating the Bag ADT.


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
        Method that adds element(s) to the bag.
        """

        # Uses append() method from DynamicArray too add an element to the bag.
        self._da.append(value)

    def remove(self, value: object) -> DynamicArray:
        """
        Method that removes element(s) from the bag.
        """

        # Counter used to count the number of iterations for the while loop.
        counter = 0

        # Loops through the array and removes identified values.  Uses get_at_index() and remove_at_index() methods
        # from DynamicArray.  Returns True if element is removed from bag, returns False otherwise.
        while counter < self._da.length():
            if self._da.get_at_index(counter) == value:
                self._da.remove_at_index(counter)
                return True
            counter += 1
        return False

    def count(self, value: object) -> int:
        """
        Method that counts the number of times an element appears in an array.
        """

        # Counter used to count the number of iterations for the while loop.
        counter = 0

        # Counts the number of times an element is counted
        plus_up = 0

        # Loops through the array and counts the number of times an element is counted.
        while counter < self._da.length():
            if self._da.get_at_index(counter) == value:
                plus_up += 1
            counter += 1
        return plus_up

    def clear(self) -> None:
        """
        Method that clears the contents of the bag
        """

        # Sets self._da to an empty DynamicArray.  Is this the right way to do this?  I couldn't think of
        # a better way at O(1) complexity.
        self._da = DynamicArray([])

    def equal(self, second_bag: "Bag") -> bool:
        """
        Method that takes two bags (arrays) and compares the contents.  If they are equal, it returns True.
        Else it returns False.
        """

        # Counter used to count the number of iterations for the while loop.
        counter = 0

        # if the two bags are not of equal length, then the result in "False"
        if self._da.length() != second_bag._da.length():
            return False

        # Loop through the different lists and compare the elements of the array (arr_el).  If they all match, return
        # true, else return false.
        while counter < self._da.length():
            arr_el = self._da.get_at_index(counter)
            if self.count(arr_el) != second_bag.count(arr_el):
                return False
            counter += 1
        return True

    def __iter__(self):
        """
        TODO: Write this implementation
        """
        self._size = 0
        self._capacity = 10
        self._data = StaticArray(self._capacity)
        counter = 0

        while counter < self._da.get_capacity():
            print(self._da.get_at_index(counter))
            counter +=1


    def __next__(self):
        """
        TODO: Write this implementation
        """
        pass

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
