class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # Pointer to parent node in tree
        self.height = 1  # Height of node in tree (max dist. to leaf)

class AVLTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return ''
        content = '\n'
        cur_nodes = [self.root]
        cur_height = self.root.height
        sep = ' ' * (2 ** (cur_height - 1))
        while True:
            cur_height -= 1
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
                if n is None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                cur_row += f' {n.value} ' + sep

                if n.left_child is not None:
                    next_nodes.append(n.left_child)
                    next_row += ' / ' + sep
                else:
                    next_row += '   ' + sep
                    next_nodes.append(None)

                if n.right_child is not None:
                    next_nodes.append(n.right_child)
                    next_row += ' \ ' + sep
                else:
                    next_row += '   ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * (len(sep) // 2)
        return content

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def _inspect_insertion(self, cur_node):
        if cur_node.parent is None:
            return

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            y = cur_node.parent
            x = cur_node
            self._rebalance_node(y, x)
            return

        cur_node.parent.height = 1 + max(self.get_height(cur_node.parent.left_child), self.get_height(cur_node.parent.right_child))
        self._inspect_insertion(cur_node.parent)

    def _rebalance_node(self, z, x):
        if x == z.left_child:
            if x.left_child:
                self._right_rotate(z)
            else:
                self._left_rotate(x)
                self._right_rotate(z)
        else:
            if x.right_child:
                self._left_rotate(z)
            else:
                self._right_rotate(x)
                self._left_rotate(z)

    def _right_rotate(self, z):
        y = z.left_child
        z.left_child = y.right_child
        if y.right_child:
            y.right_child.parent = z
        y.right_child = z
        y.parent = z.parent
        z.parent = y

        if y.parent is None:
            self.root = y
        elif y.parent.left_child == z:
            y.parent.left_child = y
        else:
            y.parent.right_child = y

        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

    def _left_rotate(self, z):
        y = z.right_child
        z.right_child = y.left_child
        if y.left_child:
            y.left_child.parent = z
        y.left_child = z
        y.parent = z.parent
        z.parent = y

        if y.parent is None:
            self.root = y
        elif y.parent.left_child == z:
            y.parent.left_child = y
        else:
            y.parent.right_child = y

        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height
