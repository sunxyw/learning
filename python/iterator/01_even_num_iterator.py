class EvenNumIterator:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        result = self.num
        self.num += 2
        return result


for i in EvenNumIterator(10):
    print(i)
