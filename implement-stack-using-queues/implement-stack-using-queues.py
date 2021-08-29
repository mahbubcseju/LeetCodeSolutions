from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qu = [Queue(), Queue()]
        self.flag = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.qu[self.flag].put(x)
        
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top = self.qu[self.flag].get()
        while not self.qu[self.flag].empty():
            self.qu[self.flag ^ 1].put(top)
            top = self.qu[self.flag].get()
        self.flag ^= 1
        return top

    def top(self) -> int:
        """
        Get the top element.
        """
        top = None
        while not self.qu[self.flag].empty():
            top = self.qu[self.flag].get()
            self.qu[self.flag ^ 1].put(top)
        self.flag ^= 1
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.qu[self.flag].empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()