class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")
        self.minStack = []
        
    def push(self, val: int) -> None:
       self.stack.append(val)
       self.minVal = min(self.minVal, val)
       self.minStack.append(self.minVal)

    def pop(self) -> None:
        print(self.stack)
        self.stack.pop()
        self.minStack.pop()
        if self.minStack == []:
            self.minVal = float("inf")
        else:
            self.minVal = self.minStack[-1]
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        
