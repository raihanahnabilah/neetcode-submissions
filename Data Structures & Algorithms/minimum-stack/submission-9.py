class MinStack:

    def __init__(self):
        self.stack = []
        self.minValStack = []
        self.minVal = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val) # O(1)
        self.minVal = min(self.minVal, val) # O(1)
        self.minValStack.append(self.minVal) # O(1)

    def pop(self) -> None:
        self.stack.pop() # O(1)
        self.minValStack.pop() # O(1)
        if self.minValStack:
            self.minVal = self.minValStack[-1]
        else:
            self.minVal = float("inf")

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        # return min(self.stack) # currently O(n)

        # for O(1), need to keep track of the minimum at every point
        return self.minValStack[-1] 
