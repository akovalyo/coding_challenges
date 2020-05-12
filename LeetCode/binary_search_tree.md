# Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

**Definition for a binary tree node:**

```python

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
```

**Example:**

```
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

***

# Solution

```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            ordered = copy.deepcopy(preorder)
            ordered.sort()
            i = 1
            for n in ordered:
                if n == root.val:
                    break
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root            
            
        return None
```