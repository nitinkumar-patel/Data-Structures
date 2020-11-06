# Level 0: 2^0 = 1 nodes
# Level 1: 2^1 = 2 nodes
# Level 2: 2^2 = 4 nodes
# Level 3: 2^3 = 8 nodes

# of nodes = 2^h - 1
# log(nodes) = height
from utils import print2D


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
                else:
                    print('Not allow to add duplicate node in BST.')
                    return

            self.number_of_nodes += 1
            return

    def search(self,data):
        if self.root is None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    def remove(self, data):
        if self.root is None:  # Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node is not None:  # Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:  # Match is found. Different cases to be checked
                # Node has left child only
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                # Node has right child only
                elif current_node.left is None:
                    if parent_node is None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # Node has neither left nor right child
                elif current_node.left is None and current_node.right is None:
                    if parent_node is None:  # Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has both left and right child
                elif current_node.left is not None and current_node.right is not None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left is not None:  # Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data  # The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right is None:  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"


if __name__=='__main__':
    tree = BinarySearchTree()
    l = [9, 4, 6, 20, 170, 15, 1]
    tree.insert(l[0])
    root=tree.root
    for i in l[1:]:
        tree.insert(i)
    print("--------------Original BST-------------------")
    print2D(root)

    tree.insert(4)  # Not allow to add duplicate node in BST.

    print(tree.search(9))  # Found
    print(tree.search(10))  # Not Found
    print(tree.search(170))  # Found

    print("--------------Remove 170-------------------")
    tree.remove(170)
    print2D(root)
    print("--------------Remove 9-------------------")
    tree.remove(9)
    print2D(root)

    """
    --------------Original BST-------------------
    
                        170
    
              20
    
                        15
    
    9
    
                        6
    
              4
    
                        1
    --------------Remove 170-------------------
    
              20
    
                        15
    
    9
    
                        6
    
              4
    
                        1
    --------------Remove 9-------------------
    
              20
    
    15
    
                        6
    
              4
    
                        1
    """