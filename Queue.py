class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def is_empty(self):
        return len(self.queue) == 0
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
    def size(self):
        return len(self.queue)





nilai = Queue()
nilai.enqueue(10)
nilai.enqueue(15)
nilai.enqueue(20)
#Mengambil nilai pertama
first = nilai.peek()
print(first)