from dsa.tree.b_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root

    def _search(self, value):
        parent = None
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None

    def insert(self, value):
        node = self._root
        if node is None:
            self._root = BinaryTreeNode(value)
        else:
            while node is not None:
                if value <= node.value():
                    if node.left() is None:
                        node.set_left(BinaryTreeNode(value))
                        break
                    else:
                        node = node.left()
                elif node.right() is None:
                    node.set_right(BinaryTreeNode(value))
                    break
                else:
                    node = node.right()

    def delete(self, value):
        if self._root is None:
            raise ValueError("Delete on an empty tree")
        node, parent = self._search(value)
        if node is None:
            raise ValueError("Value not found")
        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            if parent is None:
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else:
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None:
                new_node = BinaryTreeNode(max_node.value(), None, node.right())
            else:
                new_node = BinaryTreeNode(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            if parent is None:
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)

    def predecessor(self, value):
        node, _ = self._search(value)
        # case 1 if node has subtree, the predecessor is the max value in the left subtree
        if node.left() is not None:
            print("CASE 1: node has left subtree")
            max_node, _ = node.left().find_max_in_subtree()
            return max_node.value()

        # case 2 if node has no left subtree and is a right child, the predecessor is the parent
        if node.parent() is not None and node.parent().right() is node:
            print("CASE 2: node has no left subtree and is a right child")
            return node.parent().value()

        # case 3 if node does not have left subtree and is a left child
        current_node = node
        parent = current_node.parent()
        while parent is not None and parent.parent():
            if parent is parent.parent().right():
                print("CASE 3: node has no left subtree and is a left child")
                return parent.parent().value()
            current_node = parent
            parent = current_node.parent()

        # case 4 if we reach the root before finding such a node
        print("CASE 4: node has no predecessor")
        return node.value()

    def successor(self, value):
        node, _ = self._search(value)
        # case 1 mpde has right subtree
        if node.right() is not None:
            print("CASE 1: node has right subtree")
            min_node, _ = node.right().find_min_in_subtree()
            return min_node.value()

        # case 2 if node has no right subtree and is a left child, the successor is the parent
        if node.parent() is not None and node.parent().left() is node:
            print("CASE 2: node has no right subtree and is a left child")
            return node.parent().value()

        # case 3 if node has no right subtree and it is right child
        current_node = node
        parent = current_node.parent()
        while parent is not None and parent.parent():
            if parent is parent.parent().left():
                print("CASE 3: node has no left subtree and is a left child")
                return parent.parent().value()
            current_node = parent
            parent = current_node.parent()

        # case 4 node has no successor, since we reached the root without finding a left child
        print("case 4  node has no successor")
        return node.value()
