class iteration():
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        curent = self.start
        self.start += 1
        return curent

dataku = iteration(1,1001)
for datas in dataku :
    print (datas)