"""
SAMPLE CODE USED TO DEMONSTRATE TREE IMPLEMENTATION IN PYTHON
  USED FOR WEEK 1: REVIEW OF TREES
"""


class BinarySearchTreeKeyValue:

    class TreeNode:
        def __init__(self, key, value):
            self.parent = None
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key, value):
        n = BinarySearchTreeKeyValue.TreeNode(key, value)
        curr = self.root
        if self.is_empty():
            self.root = n
            return

        while True:
            if n.key < curr.key:
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

    def search(self, key):
        n = self._node_search(key)
        return n.value if n is not None else None

    def remove(self, key):

        node = self._node_search(key)

        # IF NO NODE IS FOUND, DO NOT DELETE AND DO NOTHING
        if node is None:
            return False

        parent = node.parent  # Thanks Tom for catching the bug last lecture :D

        # CAPTURE CHILD COUNT
        children = 0
        if node.left and node.right:
            children = 2
        elif node.left or node.right:
            children = 1

        if children == 0:  # NO CHILDREN, JUST DELETE THE NODE FROM ITS PARENT
            if parent is None:  # THIS IS JUST THE ROOT NODE W/O CHILDREN, DELETE IT
                bst.root = None
            elif parent.right is node:
                parent.right = None
            else:
                parent.left = None

        elif children == 1:  # SINGLE CHILD, JUST BYPASS IT
            next_n = None
            if node.left:
                next_n = node.left
            else:
                next_n = node.right

            if parent is None:  # THIS IS THE ROOT NODE, SPECIAL CASE
                bst.root = next_n
            elif parent.left is node:
                parent.left = next_n
            else:
                parent.right = next_n

        else:  # TWO CHILDREN - TRAVERSE TO NEXT MOST SUCCESSOR, SWAP DATA AND DELETE THE SUCCESSOR NODE
            left_parent = node
            leftmost_node = node.right
            while leftmost_node.left:
                left_parent = leftmost_node
                leftmost_node = leftmost_node.left

            node.key = leftmost_node.key
            node.value = leftmost_node.value

            if left_parent.left == leftmost_node:
                left_parent.left = leftmost_node.right
            else:
                left_parent.right = leftmost_node.right

    def get_height(self):
        return self.__get_height_of_subtree(self.root)

    def is_balanced(self):
        if self.is_empty():
            return True
        else:
            left_height = self.__get_height_of_subtree__(self.root.left)
            right_height = self.__get_height_of_subtree__(self.root.right)
            return abs(left_height - right_height) < 2

    def _get_height_of_subtree(self, node):
        if node is None:
            return 0
        else:
            left_height = 1 + self.__get_height_of_subtree__(node.left)
            right_height = 1 + self.__get_height_of_subtree__(node.right)
            return max(left_height, right_height)

    def _node_search(self, key):
        curr = self.root

        while True:
            if curr is None:
                return None
            elif curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

        return curr


if __name__ == "__main__":
    inputs = [
        {'id': 1, 'first_name': 'Eilidh', 'last_name': 'Kenny', 'address': '123 Fake St'},
        {'id': 2, 'first_name': 'Herman', 'last_name': 'Nguyen', 'address': '456 Easy St'},
        {'id': 3, 'first_name': 'Perry', 'last_name': 'Davie', 'address': '234 More St'},
        {'id': 4, 'first_name': 'Khadijah', 'last_name': 'Whittaker', 'address': '567 Taco St'},
        {'id': 5, 'first_name': 'Elowen', 'last_name': 'Neal', 'address': '111 Odd St'},
        {'id': 6, 'first_name': 'Jodie', 'last_name': 'Harvey', 'address': '222 Even St'},
        {'id': 7, 'first_name': 'Rania', 'last_name': 'Rigby', 'address': '333 Prime St'},
        {'id': 8, 'first_name': 'Manisha', 'last_name': 'Burn', 'address': '444 Fourth St'},
        {'id': 9, 'first_name': 'Dahlia', 'last_name': 'Banks', 'address': '456 Hard St'},
        {'id': 10, 'first_name': 'William', 'last_name': 'Arroyo', 'address': '987 Hollywood St'}
    ]


    # CREATE SOME BINARY TREES USING DIFFERENT KEYS
    bst = {}
    bst["by_id"] = BinarySearchTreeKeyValue()  # CREATE A TREE THAT ACCEPTS KEY VALUE PAIRS
    bst["by_first_name"] = BinarySearchTreeKeyValue()  # CREATE A TREE THAT ACCEPTS KEY VALUE PAIRS
    bst["by_address"] = BinarySearchTreeKeyValue()

    for input_ in inputs:
        bst["by_id"].insert(input_['id'], input_)
        bst["by_first_name"].insert(input_['first_name'], input_)
        bst["by_address"].insert(input_['address'], input_)

    # CREATE SOME SEARCH TESTS
    searches = {
        "by_id": [10, 8, 2],
        "by_first_name": ['William', 'Manisha', 'Herman'],
        "by_address": ['987 Hollywood St', '444 Fourth St', '456 Easy St']
    }
    assertions = [{'id': 10, 'first_name': 'William', 'last_name': 'Arroyo', 'address': '987 Hollywood St'},
                  {'id': 8, 'first_name': 'Manisha', 'last_name': 'Burn', 'address': '444 Fourth St'},
                  {'id': 2, 'first_name': 'Herman', 'last_name': 'Nguyen', 'address': '456 Easy St'}
                  ]

    for key in bst.keys():
        for s, a in zip(searches[key], assertions):
            r = bst[key].search(s)
            if r == a:
                rs = "SUCCESS"
            else:
                rs = f"FALSE expected {a} got {r}"

            print(f"BST: {key} Search for {s}, Output {r}: {rs}")

