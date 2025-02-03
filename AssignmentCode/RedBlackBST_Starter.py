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
            self.parent = None
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
            p_node = "None" if self.parent is None else self.parent.key
            p_link = " Red " if self.is_red else "Black"
            return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node}) [Parent: ({p_node})]"

    def __init__(self):
        """Creates an empty `RedBlackBST` (Red-Black Binary Search Tree)
        """
        self.root = None

### THE FOLLOWING THREE METHOD STUBS REQUIRE COMPLETION FOR ASSIGNMENT

    def insert_i(self, key, value):
        """Insert the proper value using an iterative method of traversal.
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.
        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """

        insert_node = RedBlackBST.RedBlackNode(key, value)

        # SPECIAL CASE ROOT IS EMPTY.
        if self.root is None:
            self.root = insert_node
            self.root.is_red = False
            return

        # FIND WHERE TO INSERT (TRAVERSING LEFT AND RIGHT)

        # ONCE INSERTED, TRAVERSE UP CURR.PARENT

        return

    def _rotate_left_i(self, node):
        """Perform a `rotation_left` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        return None

    def _rotate_right_i(self, node):
        """Perform a `rotation_right` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        return None

########### THE BELOW METHODS ARE FOR STUDENT USE AND CAN BE USED AS IS IN THE ITERATIVE IMPLEMENTATION

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


########### THE BELOW SECTION IS ONLY FOR REFERENCE AS A FUNCTIONING RECURSIVE IMPLEMENTATION

    def insert_r(self, key, value):
        """Insert the provided `value` at the provided `key` in the `RedBlackBST` using a recursive method `_put()`.
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.

        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """

        self.root = self._put_r(self.root, key, value)
        self.root.is_red = False

    def _put_r(self, node, key, value):
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
            node.left = self._put_r(node.left, key, value)
        elif key > node.key:
            node.right = self._put_r(node.right, key, value)
        else:
            node.value = value

        if self._right_is_red(node) and not self._left_is_red(node):
            node = self._rotate_left_r(node)
        if self._left_left_is_red(node):
            node = self._rotate_right_r(node)
        if self._left_is_red(node) and self._right_is_red(node):
            self._flip_colors(node)

        return node

    def _rotate_left_r(self, node):
        """Perform a `rotation_left` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.  Does NOT manage parent links and cannot be used for iterative
        insertion method
        :return: The new root that exists as a result of the rotation.
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right_r(self, node):
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

########### END RECURSIVE SECTION

class TestRedBlackBST:
    def __init__(self):
        self.test_keys = [10, 6, 2, 5, 4, 1, 7, 3, 9, 8]
        self.test_values = ['ten', 'six', 'two', 'five', 'four', 'one', 'seven', 'three', 'nine', 'eight']
        self.results = []

    def assert_condition(self, test_title, condition, failure_message, possible_points=1, penalty=-1):
        """Helper function to log test results"""
        if condition:
            self.results.append((test_title, True, 'Successful', possible_points, 0))
        else:
            self.results.append((test_title, False, failure_message, possible_points, penalty))

    def test_structure(self):
        """ Checks to make sure the class is named correctly and that the necessary functions are named correctly and
        that a bst can be instantiated without error. """
        try:
            bst = RedBlackBST()
        except NameError:
            self.results.append(('0.*: All Pre-Tests Failed.', False, "RedBlackBST class is Not defined", 50, -50))
            return
        except Exception as e:
            self.results.append(('0.*: All Pre-Tests Failed.', False, f"Error during instantiation: {e}", 50, -50))
            return
        else:
            self.assert_condition('0.1 RedBlackBST Exists', True, '', 1, -1)
            self.assert_condition('0.2 RedBlackBST Can be instantiated.', True, '', 1, -1)

        self.assert_condition('0.3 insert_i method exists', hasattr(bst, 'insert_i') and callable(getattr(bst, 'insert_i', None)), 'insert_i method is missing or not callable.', 1,-1)
        self.assert_condition("0.4a rotate_left_i method existence", hasattr(bst, '_rotate_left_i') and callable(getattr(bst, '_rotate_left_i', None)), "_rotate_left_i method is missing or not callable.", 1, -2)
        self.assert_condition("0.4b rotate_right_i method existence", hasattr(bst, '_rotate_right_i') and callable(getattr(bst, '_rotate_right_i', None)), "_rotate_right_i method is missing or not callable.", 1, -2)
        self.assert_condition("0.5 search method existence", hasattr(bst, 'search') and callable(getattr(bst, 'search', None)), "search method is missing or not callable.", 1, -1)
        return bst

    def test_insertion_single(self, bst):
        """Test inserting a single node into an empty Red-Black BST"""
        try:
            bst.insert_i(self.test_keys[0], self.test_values[0])
        except Exception as e:
            self.results.append(("1.* All Test 1 Failed. Exception", False, f"Exception {e}", 5, -5))
            return

        self.assert_condition("1.1 Root is not None", bst.root is not None, "bst.root is None after first insertion")
        self.assert_condition("1.2 Root is not Red", bst.root and not bst.root.is_red, "bst.root is red after insertion, should be black.")
        self.assert_condition("1.3 Root Key and Value match", bst.root and bst.root.key == self.test_keys[0] and bst.root.value == self.test_values[0], "bst.root values do not match expected values.")
        self.assert_condition("1.4 Root Left Child is None", bst.root and bst.root.left is None, "bst.root.left should be None after first insertion.")
        self.assert_condition("1.5 Root Right Child is None", bst.root and bst.root.right is None, "bst.root.right should be None after first insertion.")

        return bst  # Return BST for further testing

    def test_insertion_second(self, bst):
        """Test inserting a second node into the tree without requiring rotations"""
        try:
            bst.insert_i(self.test_keys[1], self.test_values[1])
        except Exception as e:
            self.results.append(("2.* All Test 2 Failed. Exception", False, f"Exception {e}", 5, -5))
            return

        self.assert_condition("2.1 Root.Left Should not be None", bst.root and bst.root.left is not None, "bst.root.left should not be None")
        self.assert_condition("2.2 Root.Left is connected with a red link", bst.root and bst.root.left and bst.root.left.is_red, "bst.root.left is not red")
        self.assert_condition(f"2.3 Root.left should be Key: {self.test_keys[1]}", bst.root and bst.root.left and bst.root.left.key == self.test_keys[1], f"bst.root.left.key is {bst.root.left.key}")
        self.assert_condition(f"2.4 Root Key should be Key: {bst.root.key}", bst.root and bst.root.key == 10, f"bst.root.key is not 10")
        self.assert_condition(f"2.5 Root.Left.Parent should be Root", bst.root and bst.root.left and bst.root.left.parent == bst.root, "bst.root.left.parent is not bst.root")

        return bst

    def test_insertion_third_rotate_right(self, bst):
        """Test inserting a third node that should trigger a right rotation"""
        try:
            bst.insert_i(self.test_keys[2], self.test_keys[2])
        except Exception as e:
            self.results.append(("3.* All Test 3 Failed. Exception", False, f"Exception {e}", 10, -10))
            return

        self.assert_condition(f"3.1 Root.key should be {self.test_keys[1]}", bst.root and bst.root.key == self.test_keys[1], f"bst.root.key is not {self.test_keys[1]}")
        self.assert_condition("3.2 Root.Parent should be None", bst.root and bst.root.parent is None, "bst.root.parent is not None")
        self.assert_condition(f"3.3 Root.Left should be Key: {self.test_keys[2]}", bst.root and bst.root.left and bst.root.left.key == self.test_keys[2], f"bst.root.left.key is not {self.test_keys[2]}")
        self.assert_condition("3.4 Root.Left.Parent should be Root", bst.root and bst.root.left and bst.root.left.parent == bst.root, "bst.root.left.parent is not bst.root")
        self.assert_condition("3.5 Root.Left should be connected with a black node", bst.root and bst.root.left and not bst.root.left.is_red, "bst.root.left is Red but should be Black")
        self.assert_condition("3.6 Root.Left should not have children", bst.root and bst.root.left and bst.root.left.left is None and bst.root.left.right is None, "bst.root.left has children but shouldn't")
        self.assert_condition(f"3.7 Root.Right should be Key: {bst.root.right.key}", bst.root and bst.root.right and bst.root.right.key == self.test_keys[0], f"bst.root.right.key is not 10")
        self.assert_condition("3.8 Root.Right.Parent should be Root", bst.root and bst.root.right and bst.root.right.parent == bst.root, "bst.root.right.parent is not bst.root")
        self.assert_condition("3.9 Root.Right should be connected with a black node", bst.root and bst.root.right and not bst.root.right.is_red, "bst.root.right is Red but should be Black")
        self.assert_condition("3.10 Root.Right should not have children", bst.root and bst.root.right and bst.root.right.left is None and bst.root.right.right is None, "bst.root.right has children but shouldn't")

        return bst

    def test_insertion_fourth_rotate_left(self, bst):
        """Test inserting a fourth node into the tree Which will require a rotation left."""
        try:
            bst.insert_i(self.test_keys[3], self.test_values[3])
        except Exception as e:
            self.results.append(("4.* All Test 4 Failed. Exception", False, f"Exception {e}", 10, -10))
            return

        self.assert_condition(f"4.1 Root.parent should be None", bst.root and bst.root.parent is None, "bst.root.parent is not None")
        self.assert_condition(f"4.2 Root.key should be {self.test_keys[1]}", bst.root and bst.root.key == self.test_keys[1], f"bst.root.key is not {self.test_keys[1]}")
        self.assert_condition(f"4.3 Root.Left Should be {self.test_keys[3]}", bst.root and bst.root.left.key == self.test_keys[3], f"bst.root.left.key is not {self.test_keys[3]}")
        self.assert_condition("4.4 Root.left should be black", bst.root and bst.root.left and not bst.root.left.is_red, "bst.root.left is not black")
        self.assert_condition("4.5 Root.right should be black", bst.root and bst.root.right and not bst.root.right.is_red, "bst.root.right is not black")
        self.assert_condition("4.6 Root.left.left should be red", bst.root and bst.root.left and bst.root.left.left and bst.root.left.left.is_red, "bst.root.left.left is not red")
        self.assert_condition(f"4.7 Root.Left.Left Should be {self.test_keys[2]}", bst.root and bst.root.left and bst.root.left.left and bst.root.left.left.key == self.test_keys[2], f"bst.root.left is not {self.test_keys[2]}")
        self.assert_condition("4.8 Root.Left.Right Should be None", bst.root and bst.root.left and bst.root.left.right is None, f"bst.root.left.right is not none.")
        self.assert_condition("4.9 Root.Left.Left.Left Should be none", bst.root and bst.root.left and bst.root.left.left and bst.root.left.left.left is None, "bst.root.left.left.left is not None")
        self.assert_condition("4.10 Root.Left.Left.Right Should be none", bst.root and bst.root.left and bst.root.left.left and bst.root.left.left.right is None, "bst.root.left.left.right is not None")

        return bst

    def test_insertion_fifth_rotate_left(self, bst):
        """ Inserts a few more nodes to the tree to force a few more rotations"""
        try:
            bst.insert_i(self.test_keys[4], self.test_values[4])
            bst.insert_i(self.test_keys[5], self.test_values[5])
        except Exception as e:
            self.results.append(("5.* All Tests have Failed due to exception.", False, f"Exception {e}", 10, -10))
            return

        self.assert_condition(f"5.1 Root should still be {self.test_keys[1]}", bst.root and bst.root.key == self.test_keys[1], f"bst.root is not {self.test_keys[1]}")
        self.assert_condition("5.2 Root.left should be red.", bst.root and bst.root.left and bst.root.left.is_red, "bst.root.left is not red")
        self.assert_condition(f"5.3 Root.left should be {self.test_keys[4]}", bst.root and bst.root.left and bst.root.left.key == self.test_keys[4], f"bst.left.key is not {self.test_keys[4]}")
        self.assert_condition("5.4 Root.Left.Left Should be Black", bst.root and bst.root.left and bst.root.left.left and not bst.root.left.left.is_red, "bst.root.left.left is NOT black.")
        self.assert_condition("5.5 Root.Left.Left.Parent should be Root.Left", bst.root and bst.root.left and bst.root.left.left and bst.root.left.left.parent == bst.root.left, "bst.root.left.left.parent is not bst.root.left")

        return bst

    def test_insertion_sixth_final_structure(self, bst):
        try:
            bst.insert_i(self.test_keys[6], self.test_values[6])
            bst.insert_i(self.test_keys[7], self.test_values[7])
            bst.insert_i(self.test_keys[8], self.test_values[8])
            bst.insert_i(self.test_keys[9], self.test_values[9])
        except Exception as e:
            self.results.append(("6.* All Tests have Failed.", False, f"Exception {e}", 7, -7))

        self.assert_condition(f'6.1 Root Should be {self.test_keys[4]}', bst.root and bst.root.key == self.test_keys[4], f"bst.root is not {self.test_keys[4]}")
        self.assert_condition(f'6.2 First Level (Left and Right) should be {self.test_keys[2]} and {self.test_keys[8]} respectively',
                              bst.root and bst.root.left and bst.root.left.key == self.test_keys[2] and bst.root.right and bst.root.right.key == self.test_keys[8], "bst.root.left and/or bst.root.right are incorrect.")
        self.assert_condition('6.3 Root.Right.Left Should be a Red Link',
                              bst.root and bst.root.right and bst.root.right.left and bst.root.right.left.is_red, "bst.root.right is not red")
        self.assert_condition('6.4 Root.Right.Left.Right Should be a Red Link',
                              bst.root and bst.root.right and bst.root.right.left and bst.root.right.left.right and bst.root.right.left.right.left and bst.root.right.left.right.left.is_red, "bst.root.right is not red")

        self.assert_condition('6.5 Root.Left.Left should be a black link', bst.root and bst.root.left and bst.root.left.left and not bst.root.left.left.is_red, "bst.root.left is not black")
        self.assert_condition('6.6 Root.Right.Left.Parent should be Root.Right', bst.root and bst.root.right and bst.root.right.left and bst.root.right.left.parent == bst.root.right, "bst.root.right.left's parent is incorrect.")
        self.assert_condition('6.7 Root Note should be black.', bst.root and not bst.root.is_red, "bst.root is red.  It should always be black.")

        return bst

        # self.assert_condition(f"6.1 Root Should be {self.test_keys[4]")

    def test_search_and_update(self, bst):
        try:
            first_search = bst.search(self.test_keys[0])
            test_value = 'New Test Value'
            bst.insert_i(self.test_keys[0], test_value)
            second_search = bst.search(self.test_keys[0])
        except Exception as e:
            self.results.append(("7.* All Tests have Failed.", False, f"Exception {e}", 5, -5))
            return

        self.assert_condition(f"7.1 First Search should return {self.test_values[0]}", first_search == self.test_values[0], f"bst.value is not {self.test_values[0]}")
        self.assert_condition(f"7.2 After updating second search should return {test_value}",  second_search == test_value, f"bst.value is not {test_value}, it is {second_search}")

        return bst

    def run_tests(self):
        """Run all test cases"""

        self.results.clear()

        bst = self.test_structure()

        if bst:
            bst = self.test_insertion_single(bst)
        if bst:
            bst = self.test_insertion_second(bst)
        if bst:
            bst = self.test_insertion_third_rotate_right(bst)
        if bst:
            bst = self.test_insertion_fourth_rotate_left(bst)
        if bst:
            bst = self.test_insertion_fifth_rotate_left(bst)
        if bst:
            bst = self.test_insertion_sixth_final_structure(bst)
        if bst:
            bst = self.test_search_and_update(bst)

        if not bst:
            print("Failure to run all test cases.  Look closely at your results.")

        return bst

    def print_results(self):
        if not self.results:
            print("The tests have not yet been run, please make sure to run .run_tests() before printing results.")
            return


        max_test_name = max([len(x[0]) for x in self.results])
        max_result_text = max([len(x[2]) for x in self.results])

        column_widths = [max_test_name + 2, 8, 16, max_result_text + 3]
        column_names = ['TEST NAME', 'RESULT', 'PE/PP', 'NOTE']
        header = f"{column_names[0].ljust(column_widths[0])}{column_names[1].ljust(column_widths[1])} {column_names[2].ljust(column_widths[2])}{column_names[3].ljust(column_widths[3])}"

        print(header)
        print(f"{'-' * sum(column_widths)}")

        total_possible = 0
        total_penalties = 0
        for result in self.results:
            total_possible += result[3]
            total_penalties += result[4]
            points_earned = result[3] + result[4]

            test_name_padded = result[0].ljust(column_widths[0])
            result_text = 'PASSED' if result[1] else 'FAILED'
            result_padded = result_text.ljust(column_widths[1])
            penalty_text = "" if result[4] == 0 else f"({result[4]} pts)"
            points_padded = f"{points_earned}/{result[3]} {penalty_text}".ljust(column_widths[2])
            notes_padded = f"{result[2].ljust(column_widths[3])}"

            print(f"{test_name_padded}{result_padded} {points_padded}{notes_padded}")

        total_points = total_possible + total_penalties
        print(f"{'-' * sum(column_widths)}")
        print(f"{'Points Earned (PE) / Points Possible (PP)  '.rjust(sum(column_widths[:-2]))} {total_points}/{total_possible} ({total_points*100/total_possible}%)")



if __name__ == "__main__":
    tester = TestRedBlackBST()
    bst = tester.run_tests()
    tester.print_results()
