# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):        
        self.generator = self.__call_generator(root)
        self.next_ = next(self.generator, None)
    
    def __call_generator(self, ptr, cnt=0):
        if ptr.left:
            yield from self.__call_generator(ptr.left, cnt + 1)
        yield ptr
        if ptr.right:
            yield from self.__call_generator(ptr.right, cnt + 1)
    
    def next(self) -> int:
        val = self.next_.val
        self.next_ = next(self.generator, None)
        return val

    def hasNext(self) -> bool:
        return self.next_ is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()