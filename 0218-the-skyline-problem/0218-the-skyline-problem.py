class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        from queue import PriorityQueue
        # bd_ = []
        queue = PriorityQueue()
        
        for bd in buildings:
            queue.put((bd[0], -bd[2], bd[1]))
         
        current = (-1, 0, buildings[0][0])
        ans = []
        while queue.qsize() > 0:
            top = queue.get()
            top = (top[0], -top[1], top[2])
            
            print(current, top)
            
            if current[2] < top[0]:
                ans.append([current[2], 0])
                ans.append([top[0], top[1]])
                current = (top[0], top[1], top[2])
            elif current[2] == top[0]:
                if current[1] == top[1]:
                    current= (current[0], current[1], top[2])
                else:
                    ans.append((top[0], top[1]))
                    current = top
            elif current[1] > top[1]:
                if current[2] < top[2]:
                    queue.put((current[2], -top[1], top[2]))
            elif current[1] < top[1]:
                ans.append([top[0], top[1]])
                if current[2] > top[2]:
                    queue.put((top[2], -current[1], current[2]))
                current = top
            else:
                current = (current[0], current[1], max(current[2], top[2]))
        ans.append([current[2], 0])   
        return ans
        
        