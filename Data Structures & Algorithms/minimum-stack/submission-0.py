class MinStack:

    def __init__(self):
        self.minH = []
        self.helper = []
        

    def push(self, val: int) -> None:
        if self.helper and val > self.helper[-1]:
                self.helper.append(self.helper[-1])
        else:
            self.helper.append(val)
        self.minH.append(val)
        

    def pop(self) -> None:
        self.minH.pop()
        self.helper.pop()
        

    def top(self) -> int:
        return self.minH[-1]
        

    def getMin(self) -> int:
        return self.helper[-1]
        
