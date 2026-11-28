class MinStack:

    def __init__(self):
        self.stack = []
        self.minStackVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStackVal) == 0:
            self.minStackVal.append(val)
        else:
            if val < self.minStackVal[-1]:
                self.minStackVal.append(val)
            else:
                self.minStackVal.append(self.minStackVal[-1])
        # return None

    def pop(self) -> None:
        self.stack.pop()
        self.minStackVal.pop()
        # return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStackVal[-1]
