"""
SAMPLE CODE USED TO DEMONSTRATE KEY/VALUE BST IMPLEMENTATION IN PYTHON
"""


class BinarySearchTreeKeyValue:
    """
    Standard Key/Value Binary Search Tree

    This basic class is a standard implementation of a Binary Search Tree that organizes values based on any comparable
    Key.  Keys are unique, such that if you are inserting a value into an existing key, the value stored in the original
    key slot will be replaced by the new value.
    """

    class TreeNode:
        """Basic Node for the Key/Value Binary Search Tree.

        A basic node storing a left and right child (initialized to `None`), along with a key and value.
        """
        def __init__(self, key, value):
            """Returns a newly constructed TreeNode with left and right links initialized to `None`
            :param key: The unique key by which to retrieve the desired value.  Must be comparable.
            :param value: The value in which to store in the Binary Search Tree.
            """

            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = None

        def __str__(self):
            return f"({self.key}:{self.value})"

    def __init__(self):
        """Returns newly constructed `BinarySearchTreeKeyValue` with a root initialized to `None`.
        """
        self.root = None

    def is_empty(self):
        """Returns the state of emptiness of the BinarySearchTreeKeyValue.
        :returns `True` if `self.root` is `None` (no Nodes exist in tree) and returns `False` otherwise."""
        return self.root is None

    def insert(self, key, value):
        """Insert the provided `value` at the provided `key` in the `BinarySearchTreeKeyValue`
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.
        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `BinarySearchTreeKeyValue`
        :return: `None`
        """
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
        """Search for the desired Key.
        Uses binary search to locate and return the Value at the provided Key.  If the Key is not found, `search` will
        return `None`, otherwise will return the Value stored at the key provided.
        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The Value at the Key provided, if the Key is not found, `search` will return `None`
        """
        n = self._node_search(key)
        return n.value if n is not None else None

    def remove(self, key):
        """Remove the desired Key from the `BinarySearchTreeKeyValue`.
        Searches the `BinarySearchTreeKeyValue` for the provided key.  If found, removes the key from the tree.

        :param key: The key desired to be removed from the tree.
        :return: True if the key was found and removed, False otherwise.
        """

        node = self._node_search(key)

        # IF NO NODE IS FOUND, DO NOT DELETE AND DO NOTHING
        if node is None:
            return False

        # CAPTURE CHILD COUNT
        children = 0
        if node.left and node.right:
            children = 2
        elif node.left or node.right:
            children = 1

        if children == 0:  # NO CHILDREN, JUST DELETE THE NODE FROM ITS PARENT
            if node.parent is None:  # THIS IS JUST THE ROOT NODE W/O CHILDREN, DELETE IT
                self.root = None
            elif node.parent.right is node:
                node.parent.right = None
            else:
                node.parent.left = None

        elif children == 1:  # SINGLE CHILD, JUST BYPASS IT

            if node.left:
                next_n = node.left
            else:
                next_n = node.right

            if node.parent is None:  # THIS IS THE ROOT NODE, SPECIAL CASE
                self.root = next_n
                self.root.parent = None
            elif node.parent.left is node:
                node.parent.left = next_n
                next_n.parent = node.parent
            else:
                node.parent.right = next_n
                next_n.parent = node.parent

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
                leftmost_node.right.parent = left_parent
            else:
                left_parent.right = leftmost_node.right
                leftmost_node.right.parent = left_parent

        return True

    def change_key(self, old_key, new_key):
        """Updates a Key in the tree from `old_key` to `new_key`.

        If the old_key is not found change_key will raise a KeyError Exception.
        If the new_key exists, the value at `new_key` will be replaced with the
        value that currently exists in `old_key`

        :param old_key: The original key that is desired to be changed.
        :param new_key: The new key to which the change from old key is desired.
        :return: `None`


        """
        n = self._node_search(old_key)
        if n is None:
            raise KeyError(f"{old_key} is not a valid Key.")
        else:
            v = n.value
            self.remove(old_key)
            self.insert(new_key, v)

    def get_height(self):
        """ Returns the height of the tree.

        :return: Integer height of the tree.  Returns zero if the tree is empty.
        """
        return self.__get_height_of_subtree(self.root)

    def is_balanced(self):
        """Returns True if the max difference in subtree height is less than two.  False otherwise.

        :return: `True` if max difference in subtree height is less than two, `False` otherwise.
        """
        if self.is_empty():
            return True
        else:
            left_height = self.__get_height_of_subtree__(self.root.left)
            right_height = self.__get_height_of_subtree__(self.root.right)
            return abs(left_height - right_height) < 2

    def _get_height_of_subtree(self, node):
        """ Private recursive function to determine the max height of a given subtree.

        :param node: The node for which to measure the height.
        :return: The height of the longest subtree under the provided node.
        """
        if node is None:
            return 0
        else:
            left_height = 1 + self.__get_height_of_subtree__(node.left)
            right_height = 1 + self.__get_height_of_subtree__(node.right)
            return max(left_height, right_height)

    def _node_search(self, key):
        curr = self.root

        while curr is not None:
            if curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

        return curr

class Person:
    """Toy Person class used to store a few attributes of a Person.

    This is a toy class used to demonstrate the different ways we can store data in a BST.
    """
    def __init__(self, id, first_name, last_name, address):
        """ Returns a newly formed Person object, with the following attributes: id, first & last names and address.

        :param id: An ID by which to identify the person.
        :param first_name: The person's first (or given) name.
        :param last_name: The person's last (or family) name.
        :param address: A string to represent an address of the person.
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def as_dict(self):
        """ Returns the person as a dictionary object with attributes as keys.

        :return: A dictionary representation of the `Person` object.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address
        }

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
        person = Person(input_['id'], input_['first_name'], input_['last_name'], input_['address'])
        bst["by_id"].insert(input_['id'], person)
        bst["by_first_name"].insert(input_['first_name'], person)
        bst["by_address"].insert(input_['address'], person)

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
            if r.as_dict() == a:
                rs = "SUCCESS"
            else:
                rs = f"FALSE expected {a} got {r}"

            print(f"BST: {key} Search for {s}, Output {r}: {rs}")