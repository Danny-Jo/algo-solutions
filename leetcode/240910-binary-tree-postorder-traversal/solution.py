class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        def postorder(node):
            if node is None:
                return
            
            postorder(node.left)
            
            postorder(node.right)
            
            result.append(node.val)
        
        postorder(root)
        
        return result
        