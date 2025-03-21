class TreeNode:

    def __init__(self,value):
        self.value = value
        self.left =None
        self.right =None


#Binary Search Implementation

class BinarySearchTree:

    def __init__(self):
        self.root =None

    def insert(self,value):

        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self,node,value):

        if value < node.value:
            if node.left  is None:

                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left,value)

        else:

            if node.right is None:
                node.right = TreeNode(value)
            else:

                self._insert_recursive(node.right, value)


    def search(self, value):
        return self._search_recursive(self.root, value)
    

    def _search_recursive(self, node , value):

        if not node or node.value == value:
            return value
        
        if value < node.value:

            return self._search_recursive(node.left, value)
        
        return self._search_recursive(node.right,value)
    

    def inorder_traversal(self):

        result = []

        self._inorder_recursive(self.root, result)
        return result
    


    def _inorder_recursive(self,node, result):

        if node:
            self._inorder_recursive(node.left , result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def delete(self, value):

        self.root = self._delete_recursive(self.root,value)
    
    def _delete_recursive(self, node ,value):

        if not node:
            return node
        
        if value < node.value:

            node.left = self._delete_recursive(node.left, value)

        elif value>node.value:
            node.right = self._delete_recursive(node.right, value)

        else:

            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            

            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node
            node.right = self._delete_recursive(node.right,min_larger_node.value)


        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left

        return node
    
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)

print("Inorder Traversal:", bst.inorder_traversal())  # Output: [2, 5, 7, 10, 12, 15, 20]

print("Search 7:", bst.search(7) is not None)  # Output: True
print("Search 25:", bst.search(25) is not None)  # Output: False

bst.delete(10)
print("Inorder Traversal After Deletion:", bst.inorder_traversal())  

        

        