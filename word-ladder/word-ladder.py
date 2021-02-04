class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import OrderedDict, deque
        
        words = OrderedDict()
        queue = deque()
        
        wordList.append(beginWord)
        for i, word in enumerate(wordList):
            words[word] = i
        
        visited = [0] * len(wordList)
        visited[words[beginWord]] = 1
        queue.append(words[beginWord])
        while len(queue):
            x = queue.popleft()
            curWord = wordList[x]
            for j, ch in enumerate(curWord):
                for kch in range(ord('a'), ord('z') + 1):
                    chng = curWord[:j] + chr(kch) + curWord[j + 1:]
                    if chng in words and visited[words[chng]] == 0:
                        visited[words[chng]] = visited[x] + 1
                        queue.append(words[chng])
                        
        return visited[words[endWord]] if endWord in words else 0