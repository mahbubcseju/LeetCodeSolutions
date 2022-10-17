# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from queue import Queue
        
        st = []
        qu = Queue()
        qu.put(root)
        while qu.qsize() > 0:
            fr = qu.get()
            if fr == None:
                st.append('_')
            else:
                st.append(str(fr.val))
                qu.put(fr.left)
                qu.put(fr.right)
        
        return ','.join(st)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if data[0] =='_':
            return None
        from queue import Queue
        qu = Queue()
        ptr = 0
        root = TreeNode(data[0])
        qu.put(root)
        
        while qu.qsize() > 0:
            fr = qu.get()
            if data[ptr + 1] != '_':
                fr.left = TreeNode(data[ptr + 1])
                qu.put(fr.left)
            if data[ptr + 2] != '_':
                fr.right = TreeNode(data[ptr + 2])
                qu.put(fr.right)
            ptr += 2
        return root
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))