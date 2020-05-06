#!python

from linkedlist import LinkedList

# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests


class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.list.size == 0

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because appending at end you can just use tail pointer"""
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list.head.data  # first item in linkedlist

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) because deleting the first item only uses head pointer"""
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError

        front = self.list.head.data
        self.list.delete(front)
        return front

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests


class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because dynamic arrays have extra empty spaces,when push it
        fills up empty space """
        # Insert given item
        self.list.append(item)  # inserts item at end

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list[0]  # first item of the list

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n-i) because array item shift to the left"""
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError

        front = self.list[0]  # first item
        self.list.pop(0)  # delete first item
        return front  # return front


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue