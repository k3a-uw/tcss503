class RedBlackBST:
    class RedBlackNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = None
            self.left = None
            self.right = None
            self.is_red = True  # NEW NODES ARE ALWAYS RED IN THIS IMPLEMENTATION TO DEFAULT THEM TO BE SO.

        def __str__(self):
            l_node = "None" if self.left is None else self.left.key
            l_link = "Black" if self.left is None or not self.left.is_red else " Red "
            r_node = "None" if self.right is None else self.right.key
            r_link = "Black" if self.right is None or not self.right.is_red else " Red "
            return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node})"

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.is_red = False

    def search(self, key):
        n = self._node_search(key)
        return n.value if n is not None else None

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

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _flip_colors(self, node):
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False

    def _put(self, node, key, value):
        if node is None:
            return RedBlackBST.RedBlackNode(key, value)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        # CONTROL FOR NULL LINKS (NULL LINKS CAN BE CONSIDERED BLACK IN THIS CONTEXT
        right_is_red = node.right is not None and node.right.is_red
        left_is_red = node.left is not None and node.left.is_red
        left_left_is_red = left_is_red and node.left.left is not None and node.left.left.is_red

        if right_is_red and not left_is_red:
            node = self._rotate_left(node)
        if left_left_is_red:
            node = self._rotate_right(node)
        if left_is_red and right_is_red:
            self._flip_colors(node)

        return node


class Person:
    def __init__(self, id, first_name, last_name, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Person:
    def __init__(self, id, first_name, last_name, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def as_dict(self):
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
