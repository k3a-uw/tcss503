"""
SAMPLE CODE USED TO DEMONSTRATE TREE IMPLEMENTATION IN PYTHON
  USED FOR WEEK 1: REVIEW OF TREES
"""


class BinarySearchTreeDynamic:

    class TreeNode:
        def __init__(self, data):
            self.parent = None
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, max_children=2):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        n = BinarySearchTreeDynamic.TreeNode(data)
        if self.is_empty():
            self.root = n
        else:
            curr = self.root
            parent = None
            while True:
                parent = curr
                if n.data < curr.data:
                    curr = curr.left
                    if not curr:
                        parent.left = n
                        return
                else:
                    curr = curr.right
                    if not curr:
                        parent.right = n
                        return

    def search(self, data):
        curr = self.root

        while True:
            if not curr:
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
    inputs = [10, 5, 20, 25, 20]
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

    inputs = [10, 5, 20, 25, 20]
    bst = BinarySearchTreeSequential()  # CREATE A TREE THAT RUNS WITH NODES
    for input in inputs:
        bst.insert(input)

    outputs = [(10, 0), (20, 2), (25, 5)]

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
