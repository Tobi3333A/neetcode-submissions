class MinStack:

    def __init__(self):
        self.arr = []
        self.low = 0
        self.pref = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.pref:
            self.pref.append(val)
        else:
            if val < self.pref[-1]:
                self.pref.append(val)
            else:
                self.pref.append(self.pref[-1])

    def pop(self) -> None:
        self.pref.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.pref[-1]
