#!python

from queue import LinkedQueue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""

        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""

        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: O(1) if the node is leaf,
        O(n) function height have to be called n amount of times to return value """

        left_height = 0
        right_height = 0

        if self.left is None and self.right is None:
            return 0

        # Check if left child has a value and if so calculate its height
        if self.left is not None:
            left_height = self.left.height()

        # Check if right child has a value and if so calculate its height
        if self.right is not None:
            right_height = self.right.height()

        # Return one more than the greater of the left height and right height
        return max(left_height, right_height) + 1


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        # Check if root node has a value and if so calculate its height
        if self.root != None:
            return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: log(n) under what conditions? If tree is balanced
        Worst case running time: O(n) under what conditions? If tree is structured as a list """

        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)

        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: log(n) under what conditions? If tree is balanced
        Worst case running time: O(n) under what conditions? If tree is structured as a list in one direction"""

        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)

        #  Return the node's data if found, or None
        if node:
            return node.data
        return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: log(n) under what conditions? if its a balanced 
        tree you can insert item by removing half of the tree.
        TODO: Worst case running time: 0(n) under what conditions? if it was a linear tree"""

        # Handle the case where the tree is empty
        if self.is_empty():

            # Create a new root node
            self.root = BinaryTreeNode(item)

            # Increase the tree size
            self.size += 1
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)

        # Check if the given item should be inserted left of parent node
        if parent.data > item:

            # Check if the given item should be inserted right of parent node
            parent.left = BinaryTreeNode(item)

        elif parent.data < item:

            # Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)

        #  Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: log(n) under what conditions? If tree is balanced
        TODO: Worst case running time: O(n) under what conditions? If tree is unbalanced"""

        # Start with the root node
        node = self.root

        # Loop until we descend past the closest leaf node
        while node is not None:

            # Check if the given item matches the node's data
            if item == node.data:

                # Return the found node
                return node

            # Check if the given item is less than the node's data
            elif item < node.data:

                # Descend to the node's left child
                node = node.left

            #  Check if the given item is greater than the node's data
            elif item > node.data:

                # Descend to the node's right child
                node = node.data

        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: O(log n) under what conditions?
        If its a balanced tree
        TODO: Worst case running time: O(n) under what conditions?
        If the tree structure is lop sided or one direction """

        # Check if starting node exists
        if node is None:

            # Not found (base case)
            return None

        # Check if the given item matches the node's data
        elif node.data == item:

            # Return the found node
            return node

        # Check if the given item is less than the node's data
        elif item < node.data:

            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)

        # Check if the given item is greater than the node's data
        elif item > node.data:

            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: log(n) under what conditions? if tree is balanced
        TODO: Worst case running time: O(n) under what conditions? if tree lop sided, unbalanced"""

        # Start with the root node and keep track of its parent
        node = self.root

        parent = None

        # Loop until we descend past the closest leaf node
        while node is not None:

            # Check if the given item matches the node's data
            if item == node.data:

                # Return the parent of the found node
                return parent

            # Check if the given item is less than the node's data
            elif item < node.data:

                # Update the parent and descend to the node's left child
                parent = node
                node = node.left

            # Check if the given item is greater than the node's data
            elif item > node.data:

                # Update the parent and descend to the node's right child
                parent = node

                node = node.right

        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion).
        Best case running time: O(1) if node is root, parent is none
        Worst case running time: log(n) binary search  tree
        """

        # Check if starting node exists
        if node is None:  # no nodes

            # Not found (base case)
            return None

        # Check if the given item matches the node's data
        if item == node.data:

            # Return the parent of the found node
            return parent  # returns None if it's root node

        # Check if the given item is less than the node's data
        elif item < node.data:

            # Recursively descend to the node's left child, if it exists
            if node.left is None:
                return node  # node will be the parent if we want to insert the item

            else:
                # return node if node.left is None else self._find_parent_node_recursive(item, node.left, node)
                return self._find_parent_node_recursive(item, node.left, node)

        # Check if the given item is greater than the node's data

        elif item > node.data:

            # Recursively descend to the node's right child, if it exists
            # return node if node.right is None else self._find_parent_node_recursive(item, node.right, node)

            if node.right is None:
                return node  # node will be the parent if we want to insert the item
            else:
                return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: O(logn) if item is a leaf node
        Worst case running time: O(n) if item has 2 children. Called
        find_min_right helper function to makes it O(n)"""
        # Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

        node = self._find_parent_node_iterative(item)
        if node is None:
            raise ValueError

        # Leaf node
        if node.left is None and node.right is None:

            # if node is root
            if node == self.root:

                # delete root node
                self.root = None
                return

            # assign parent
            parent = self._find_parent_node_iterative(node.data)

            # check wether the parent is greater or less than the child
            if node.data < parent.data:  # if node is on left side
                parent.left = None
            else:
                parent.right = None

        elif node.left is None and node.right is not None:  # has only right child

            # find it's parent
            parent = self._find_parent_node_iterative(node.data)

            # parent will point to the child of the node we want to delete
            parent.right = node.right

        elif node.right is None and node.left is not None:  # only left child

            # find it's parent
            parent = self._find_parent_node_iterative(node.data)

            # parent will point to the child of the node we want to delete
            parent.left = node.left

        else:  # if it has both a left and a right
            # find successor of the node (the minimum in right subtree)

            minimum_right = self.find_min_right(node)  # O(n)

            # copy the value of the minimum to the target node
            temp = minimum_right

            # delete the duplicate (minimum right subtree)
            self.delete(minimum_right)

            # copy the value of the minimum to the target node
            node.data = mininmum_right

    def find_min_right(self, node):
        in_order_items = self.items_in_order()
        node_index = in_order_items.index(node.data)
        next_node_index = node_index + 1
        return in_order_items[next_node_index]

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""

        items = []

        if not self.is_empty():

            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)

        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) traversing through node, O(1) operation per node
        Memory usage: O(h) or O(logn) the call stack doesn't exceed height"""

        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)

        # Visit this node's data with given function
        visit(node.data)

        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""

        items = []

        if not self.is_empty():

            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)

        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) traversing through node, O(1) operation per node
        Memory usage: O(h) or O(logn) the call stack doesn't exceed height"""

        # Visit this node's data with given function
        visit(node.data)

        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)

        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []

        if not self.is_empty():

            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)

        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) traversing through node, O(1) operation per node
        Memory usage: O(h) or O(logn) the call stack doesn't exceed height"""

        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)

        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)

        # Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        pass
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""

        items = []

        if not self.is_empty():

            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)

        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because there is O(1) operation on each node
        Memory usage: O(width) the stack won't exceed the width of the level it's in"""

        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()

        # Enqueue given starting node
        queue.enqueue(start_node)

        # Loop until queue is empty
        while not queue.is_empty():

            # Dequeue node at front of queue
            node = queue.dequeue()

            # Visit this node's data with given function
            visit(node.data)

            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)

            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()