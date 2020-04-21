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