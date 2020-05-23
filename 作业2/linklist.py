
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkList:
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.head = node

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def travel(self):  # 遍历整个列表
        cur = self.head
        while cur != None:
            print(cur.key, end=' ')
            cur = cur.next
        print("\n")

    def add(self, obj):  # 链表头部添加元素
        node = Node(obj)
        node.next = self.head
        self.head = node

    def append(self, obj):  #链表尾部添加元素
        node = Node(obj)
        node.next = None
        a = self.head
        if self.head == None:
            self.head = node
        else:
            while(a.next!=None):
                a = a.next
            a.next = node


    def insert(self, pos, obj):  #在链表的pos处插入关键字为obj的元素
        node = Node(obj)
        s = self.head
        for i in range(pos-1):
            s = s.next
        node.next = s.next
        s.next = node
        
    def search(self, obj):  #查询关键字为obj的结点
        s = self.head
        k = 1
        while (s.key != obj):
            s = s.next
            k += 1 
        return k

    def remove(self, obj):  #删除所有关键字为obj的结点
        a = self.head
        b = a.next
        if a.key == obj:
            a = a.next
            b = b.next
            self.head = self.head.next
        while(b.next != None):
            if b.key == obj:
                b = b.next
                a.next = b
            else:
                a = a.next
                b = b.next
        if b.key == obj:
            a.next = None

    def length(self): #求链表长度
        length = 0
        s = self.head
        while (s.next != None):
            s = s.next
            length += 1
        length += 1 #算上尾结点
        return length


print("学号 201715262")
student_number_list = [2,0,1,7,1,5,2,6,2]
student_number_linklist = LinkList()         #创建链表

student_number_linklist.isEmpty()
for i in student_number_list:   #逐个放入链表
    student_number_linklist.append(i)
    
student_number_linklist.travel()
print("是否为空:{}".format(student_number_linklist.isEmpty()))
print("最大值是7，删除7")
student_number_linklist.remove(7)
student_number_linklist.travel()
print("测试add方法")
student_number_linklist.add(3)
student_number_linklist.travel()
print("测试insert方法")
print("在第5位后边插入8")
student_number_linklist.insert(5,8)
student_number_linklist.travel()
print("测试search方法,查询5在第几位")
print(student_number_linklist.search(5))
print("长度是{}".format(student_number_linklist.length()))
