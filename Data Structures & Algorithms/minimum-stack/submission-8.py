class MinStack:
    # 1, 
    # min = 1
    # 2 
    # min = 1
    # 0 
    # min = 0
    # pop()
    # min = 1
    # prevMin?
    # keep track of another stack
    # [1, 1]

    def __init__(self):
        self.stack = []
        self.minVal = 2**31
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val) 
        self.minVal = min(val, self.minVal)
        self.minStack.append(self.minVal)

    def pop(self) -> None:
        self.stack.pop()    
        self.minStack.pop() 
        if len(self.minStack) == 0:
            self.minVal = 2**31
        else:
            self.minVal = self.minStack[len(self.minStack) - 1]  

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        # return min(self.stack) # this is not O(1) though. at most O(n)
        
        return self.minStack[len(self.minStack) - 1]
