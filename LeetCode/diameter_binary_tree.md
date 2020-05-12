# Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


**Example:**

```
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
```
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

**Definition for a binary tree node:**

***

# Solution

```python

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

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
```
