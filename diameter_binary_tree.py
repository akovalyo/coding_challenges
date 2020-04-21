class Solution:
    def len_tree(self, node: TreeNode) -> int:
        if node is None:
            return 0 
        return 1 + max(self.len_tree(node.left), self.len_tree(node.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        l_len = self.len_tree(root.left)
        r_len = self.len_tree(root.right)
        max_diameter = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(l_len + r_len, max_diameter)