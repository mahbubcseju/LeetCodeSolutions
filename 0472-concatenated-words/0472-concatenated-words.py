class Solution:
        
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        class Tree:
            def __init__(self, val = 0):
                self.val = val
                self.next_ = [-1 for j in range(26)]
        
        def insert_word(root, word):
            ptr = root
            for x in word:
                k = ord(x) - ord('a')
                if ptr.next_[k] == -1:
                    ptr.next_[k] = Tree()
                ptr = ptr.next_[k]
            ptr.val = 1
        
        def query(root, word):
            ptr = root
            for x in word:
                k = ord(x) - ord('a')
                if ptr.next_[k] == -1:
                    return False
                ptr = ptr.next_[k]
            return ptr.val == 1
        
        root = Tree()
        for word in words:
            insert_word(root, word)
        
        ans = []
        for word in words:
            len_ = len(word)
            dp = [-1 for i in range(len_ + 1)]
            dp[0] = 0
            for j in range(1, len_ + 1):
                if dp[j-1] == -1:
                    continue
                for k in range(j, len_ + 1):
                    temp_word = word[j - 1: k]
                    if query(root, temp_word):
                        dp[k] = max(dp[k], dp[j-1] + 1)
            if dp[len_] >= 2:
                ans.append(word)
        
        return ans
