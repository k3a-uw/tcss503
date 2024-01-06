"""
SAMPLE CODE USED TO DEMONSTRATE TREE IMPLEMENTATION IN PYTHON
  USED FOR WEEK 1: REVIEW OF TREES
"""
from collections import deque

class BinarySearchTreeDynamic:

    class TreeNode:
        def __init__(self, data):
            self.parent = None
            self.data = data
            self.left = None
            self.right = None

    def __str__(self):
        q = deque()
        if self.is_empty():
            print("Empty")

    def __init__(self, max_children=2):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        n = BinarySearchTreeDynamic.TreeNode(data)
        curr = self.root
        if self.is_empty():
            self.root = n
            return

        while True:
            if n.data < curr.data:
                if curr.left is None:
                    n.parent = curr
                    curr.left = n
                    return
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    n.parent = curr
                    curr.right = n
                    return
                else:
                    curr = curr.right

    def search(self, data):
        curr = self.root

        while True:
            if curr is None:
                return None
            elif curr.data == data:
                return data
            elif curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        return curr

    def get_height(self):
        return self.__get_height_of_subtree(self.root)

    def __get_height_of_subtree__(self, node):
        if node is None:
            return 0
        else:
            left_height = 1 + self.__get_height_of_subtree__(node.left)
            right_height = 1 + self.__get_height_of_subtree__(node.right)
            return max(left_height, right_height)

    def is_balanced(self):
        if self.is_empty():
            return True
        else:
            left_height = self.__get_height_of_subtree__(self.root.left)
            right_height = self.__get_height_of_subtree__(self.root.right)
            return abs(left_height - right_height) < 2


class BinarySearchTreeSequential:

    def __init__(self, init_size=64):
        self.data = [None] * init_size
        self.count = 0

    def __expand__(self):
        self.data = self.data + [None] * len(self.data)

    def __get_idx_of_left__(self, index):
        return 2 * index + 1

    def __get_idx_of_right__(self, index):
        return 2 * index + 2

    def __get_idx_of_parent__(self, index):
        """ Returns the parent of a given index.  Returns -1 for root."""
        offset = 1 if index % 2 == 1 else 2
        return (index - offset) // 2

    def is_empty(self):
        return self.data[0] is None

    def insert(self, data):
        if self.is_empty():
            self.data[0] = data
        else:
            idx = 0
            while self.data[idx] is not None:
                if data < self.data[idx]:
                    idx = self.__get_idx_of_left__(idx)
                else:
                    idx = self.__get_idx_of_right__(idx)

                if idx > len(self.data) - 1:  # YOU HAVE REACHED
                    self.__expand__()

            self.data[idx] = data
            self.count += 1

    def search(self, data):
        idx = 0
        while self.data[idx] is not None:
            if data == self.data[idx]:
                return idx
            elif data < self.data[idx]:
                idx = self.__get_idx_of_left__(idx)
            else:
                idx = self.__get_idx_of_right__(idx)

            if idx > len(self.data) - 1:
                return None




if __name__ == "__main__":
    inputs = [10, 5, 20, 25, 15]
    bst = BinarySearchTreeDynamic()  # CREATE A TREE THAT RUNS WITH NODES
    for input in inputs:
        bst.insert(input)

    outputs = [10, 20, 25]

    for output in outputs:
        r = bst.search(output)
        if r == output:
            rs = "SUCCESS"
        else:
            rs = f"FALSE expected {output} got {r}"

        print(f"Testing for Output {output}: {rs}")

    inputs = [10, 5, 20, 25, 15, 27, 26]
    bst = BinarySearchTreeSequential()  # CREATE A TREE THAT RUNS WITH NODES
    for input in inputs:
        bst.insert(input)

    outputs = [(10, 0), (20, 2), (25, 6)]

    for output in outputs:
        r = bst.search(output[0])
        if r == output[1] and bst.data[r] == output[0]:
            rs = "SUCCESS"
        else:
            rs = f"FALSE expected {output} got ({bst.data[r]}, {r})"

        print(f"Testing for Output {output}: {rs}")

    for i in range(1, 20):
        print(f"Inserting {i}")
        bst.insert(i)

    print(f"How bloated is it: BST Contains {bst.count} records in an array of size {len(bst.data)}")