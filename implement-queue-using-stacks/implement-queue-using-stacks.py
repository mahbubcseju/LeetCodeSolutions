from queue import LifoQueue
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qu = [LifoQueue(), LifoQueue()]
    
    def transform(self):
        if self.qu[1].empty():
            while not self.qu[0].empty():
                self.qu[1].put(self.qu[0].get())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.qu[0].put(x)
    

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.transform()
        return self.qu[1].get()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.transform()
        top = self.qu[1].get()
        self.qu[1].put(top)
        return top


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        self.transform()
        return self.qu[1].empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()