class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current
    

print(CountDown(3))