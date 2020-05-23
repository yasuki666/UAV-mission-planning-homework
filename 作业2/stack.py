class stack():
    top = 0
    list = []

    def __init__(self,some_list=[]):
        self.list = some_list
        self.top = len(some_list)

    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self,obj):
        self.list.append(obj)
        self.top+=1

    def pop(self):
        if self.top>0:
            self.list.pop()
            self.top -=1
        else:
            pass


#测试
a = stack([1,2,3])
b = stack()
print(a.isEmpty())
print(b.isEmpty())
print(a.list)
a.push(4)
print(a.list)
a.pop()
print(a.list)
print(a.top)
a.pop()
a.pop()
a.pop()
print(a.list)
print(a.top)
a.pop()
print(a.list)
print(a.top)