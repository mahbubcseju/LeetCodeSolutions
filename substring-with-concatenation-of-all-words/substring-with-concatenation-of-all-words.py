class Node(object):
    def __init__(self, val=None):
        self.val = None
        self.next = [None] * 26

class Solution(object):
    def insert(self, cur, word, i_d):
        for ch in word:
            x = ord(ch) - ord('a')
            if not cur.next[x]:
                cur.next[x] = Node()
            cur = cur.next[x]
        if cur.val == None:
            cur.val = i_d
            return i_d + 1
        return i_d
        
    def query(self, cur, s):
        for ch in s:
            x = ord(ch) - ord('a')
            if not cur.next[x]:
                return None
            cur = cur.next[x]
        return cur.val
    
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        head = Node()
        tot = 0
        for ind, word in enumerate(words):
            tot = self.insert(head, word, tot)
        countt = [0] * tot
        for ind, word in enumerate(words):
            k = self.query(head, word)
            countt[k] += 1
        
        total_word = len(words)
        length_of_each = len(words[0])
        
        result = []
        for k in range(length_of_each):
            counter = [0] * tot
            total = 0
            st = k
            for i in range(k + length_of_each - 1, len(s), length_of_each):
                sub = self.query(head, s[i - length_of_each + 1: i + 1])
                if sub == None:
                    st = i + 1
                    total = 0
                    counter = [0] * tot
                    continue
                    
                counter[sub] += 1
                if counter[sub] == countt[sub]:
                    total += 1
                while counter[sub] > countt[sub]:
                    sub_first = self.query(head, s[st: st + length_of_each])
                    counter[sub_first] -= 1
                    if counter[sub_first] == countt[sub_first] - 1:
                        total -= 1
                    st += length_of_each
                    
                if total == tot:
                    result.append(i - total_word * length_of_each + 1)
                # print(k, counter, total, countt)
        return result
                    
                
        
        