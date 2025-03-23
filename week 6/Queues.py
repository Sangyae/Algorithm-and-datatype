class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == [] 
    def size(self):
        return len(self.items)  
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()

# class Queue:
#    def __init__(self):
#        self.items = []
#    def is_empty(self):
#        return self.items == []
#    def size(self):
#        return len(self.items)
#    def enqueue(self, item):
#        self.items.insert(0,item)  
#    def dequeue(self):
#        return self.items.pop()
   
try:
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    while not q.is_empty():
        print(q.dequeue())
except IndexError:
    print('empty queue')