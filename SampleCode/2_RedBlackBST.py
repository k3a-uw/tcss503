class RedBlackBST:
    """ A Python Implementation of a Red-Black Binary Search Tree
    """
    class RedBlackNode:
        """Basic node representing the Key/Value and color of a link/node.
        """
        def __init__(self, key, value):
            """Returns a newly created `RedBlackNode` initiated to be a "Red" link.
            :param key: The unique, comparable object by which to retrieve the desired value.
            :param value: The value in which to store in the `RedBlackBST` object.
            """
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.is_red = True  # NEW NODES ARE ALWAYS RED IN THIS IMPLEMENTATION TO DEFAULT THEM TO BE SO.

        def __str__(self):
            """Returns a string representation of a node, including the ids and colors of its left and right links.
            The pattern used is: `(left.key)<-[Red|Black]--(node.key)--[Red|Black]->(right.key)
            If either left or right nodes are blank, the key is `None` and the link color defaults to `Black`.

            :return: String representation of the desired node.
            """
            l_node = "None" if self.left is None else self.left.key
            l_link = "Black" if self.left is None or not self.left.is_red else " Red "
            r_node = "None" if self.right is None else self.right.key
            r_link = "Black" if self.right is None or not self.right.is_red else " Red "
            return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node})"

    def __init__(self):
        """Creates an empty `RedBlackBST` (Red-Black Binary Search Tree)
        """
        self.root = None

    def insert(self, key, value):
        """Insert the provided `value` at the provided `key` in the `RedBlackBST` using a recursive method `_put()`.
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.

        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """

        self.root = self._put(self.root, key, value)
        self.root.is_red = False

    def search(self, key):
        """Search for the desired Key.
        Uses binary search to locate and return the Value at the provided Key.  If the Key is not found, `search` will
        return `None`, otherwise will return the Value stored at the key provided.
        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The Value at the Key provided, if the Key is not found, `search` will return `None`
        """
        n = self._node_search(key)
        return n.value if n is not None else None

    def _node_search(self, key):
        """ Searches for the desired key and returns the `RedBlackNode` associated to that key.

        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The `RedBlackNode` at the Key provided, if the Key is not found, `_node_search` will return `None`
        """
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

    def _rotate_left(self, node):
        """Perform a `rotation_left` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right(self, node):
        """Perform a `rotation_right` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _flip_colors(self, node):
        """Using the provided `node`, set both child links to black, and set the parent link to `Red`.
        :param node: The node for which the child colors and parent link should have their colors flipped.
        :return: None
        """
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False

    def _right_is_red(self, node):
        """Indicates whether the link to the right of the provided node is currently Red.
        :param node: The node of which the right link is viewed for redness.
        :return: `True` if `node.right` is red, `False` otherwise.
        """
        if node.right is None:
            return False
        else:
            return node.right.is_red

    def _left_is_red(self, node):
        """Indicates whether the link to the left of the provided node is currently Red.
        :param node: The node of which the left link is viewed for redness.
        :return: `True` if `node.left` is red, `False` otherwise.
        """
        if node.left is None:
            return False
        else:
            return node.left.is_red

    def _left_left_is_red(self, node):
        """Indicates whether there exists to consecutive left red links from the given node.
        :param node: The node from which to interrogate the left and left.left nodes for redness.
        :return: `True` if `node.left` is red and 'node.left.left` is red.  `False` otherwise.
        """
        if node is None:
            return False
        else:
            return self._left_is_red(node) and self._left_is_red(node.left)

    def _put(self, node, key, value):
        """A recursive call to insert a new value into the structure using the standard Red-Black insertion rules.
        Base Case: The Node provided is None, in which case, create a new `RedBlackNode` and return.
        Recursive Case: If the insertion key is equal to node.key. replace the value and return (special case).  If the
        insertion key is less than node.key, resurcively _put into node.left, otherwise recursively _put into node.right

        After the base case if found, recursively check for necessary rotations and color flips.

        :param node: The `RedBlackNode` into which a _put is attempted.
        :param key: The desired key to insert into the `RedBlackBST`
        :param value: The desired value to store at the provided `key`.
        :return: Returns the parent node from the level of recursion that has been executed.
        """
        if node is None:
            return RedBlackBST.RedBlackNode(key, value)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        if self._right_is_red(node) and not self._left_is_red(node):
            node = self._rotate_left(node)
        if self._left_left_is_red(node):
            node = self._rotate_right(node)
        if self._left_is_red(node) and self._right_is_red(node):
            self._flip_colors(node)

        return node


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
    bst["by_id"] = RedBlackBST()  # CREATE A TREE THAT ACCEPTS KEY VALUE PAIRS
    bst["by_first_name"] = RedBlackBST()  # CREATE A TREE THAT ACCEPTS KEY VALUE PAIRS
    bst["by_address"] = RedBlackBST()

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
