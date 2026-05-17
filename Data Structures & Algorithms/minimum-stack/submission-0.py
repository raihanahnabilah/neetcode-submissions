class MinStack:

    def __init__(self):
        self.array = []
        

    def push(self, val: int) -> None:
        self.array.insert(0, val)

    def pop(self) -> None:
        self.array.pop(0)
        
    def top(self) -> int:
        return self.array[0]
        
    def getMin(self) -> int:
        return min(self.array);
