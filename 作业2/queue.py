
class queue():
    head = 0
    tail = 0
    list = []
    queue = []

    def __init__(self,some_list=[]):
        self.list = some_list
        self.head = 1
        self.tail = len(some_list)+1
        self.queue = self.list

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def dequeue(self):
        if self.head<self.tail:
            self.head +=1
            self.queue = self.list[self.head-1:self.tail]

    def enqueue(self,obj):
        self.list.append(obj)
        self.tail +=1
        self.queue = self.list[self.head-1:self.tail]


#测试
c = queue([1,2,3])
d = queue()
print(c.isEmpty())
print(d.isEmpty())
print(c.queue)
c.enqueue(4)
print(c.list)
print(c.queue)
c.dequeue()
print(c.queue)
c.dequeue()
print(c.queue)
c.dequeue()
print(c.queue)
c.dequeue()
print(c.queue)
c.dequeue()
print(c.queue)

d.enqueue(4)
print(d.queue)
print(d.head)
print(d.tail)
d.dequeue()
print(d.queue)
d.dequeue()
print(d.queue)
print(d.head)
print(d.tail)
print(d.isEmpty())
d.enqueue(4)
print(d.queue)
print(d.isEmpty())
d.dequeue()
print(d.head)
print(d.tail)
print(d.isEmpty())