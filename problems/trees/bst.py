class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    

    def inorder(self):
        return []
    
    def min_item(self):
        return None
    
    def max_item(self):
        return None


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        if self.is_empty():
            return []
        return self.ascending_helper([])

    def ascending_helper(node, traversal):
        if node.is_empty():
            return []
        if not node.left.is_empty():
            node.left.ascending_helper(traversal)
        traversal.append(node.value)
        if not node.right.is_empty():
            node.right.ascending_helper(traversal)
        return traversal
    
    def min_item(self):
        if self.is_leaf():
            return self.value
        return self.left.min_item()
    
    def max_item(self):
        if self.is_leaf():
            return self.value
        return self.right.max_item()

if __name__ == "__main__":
    bst = Empty().insert(42)
    bst = bst.insert(60).insert(17).insert(29).insert(5).insert(53)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(f"The list of nodes is {bst.inorder()}")
    print(f"The minimum value is {bst.min_item()}")
