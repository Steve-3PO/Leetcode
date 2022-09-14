# Min Stack

class MinStack:

    # create the initial conditions of the class, a stack and a minimumstack tracker
    def __init__(self):
        self.stack = []
        self.minstack = []

    # always want to add to the stack, but only to the minstack if the new value is smaller     than the last
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    
    # pop both values
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    # return the last element in the stack
    def top(self) -> int:
        return self.stack[-1]

    # return the last element in the stack
    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()