#汉诺塔问题
def Hannuota(n,A,C):#传入3个参数，n是盘子的个数，A是起始的柱子，C是要放入的柱子
    if n==1:
        print("{}号：{}->{}".format(n,A,C))
    else:
        list1 = ['A','B','C']
        list1.remove(A)
        list1.remove(C)
        a = A
        b = list1[0]
        c = C
        Hannuota(n-1,a,b)
        print("{}号：{}->{}".format(n,A,C))
        Hannuota(n-1,b,c)


def find_fake_3(coin_list):    #3枚硬币找其中1个假币，len(coin_list) = 3
    if coin_list[0]>coin_list[1]:
        return 1,1   #两个返回值，第一个是所在位置，第二个是比较次数
    elif coin_list[0]<coin_list[1]:
        return 0,1
    else:
        return 2,1


def sum(test_list): #数列求和函数
    s = 0
    for i in test_list:
        s += i
    return s

def find_fake_3n(coin_list):      #len(coin_list) = 3^n
    length = len(coin_list)
   
    if length == 3:     #递归结束条件
        s = find_fake_3(coin_list)
        return s
    else:
        #先分成三份，每份3^(n-1)枚硬币"
        head_list = coin_list[:length//3]
        mid_list = coin_list[length//3:2*length//3]
        tail_list = coin_list[2*length//3:]
        if sum(head_list)<sum(mid_list):
            s=find_fake_3n(head_list)
            return s[0],s[1]+1
        elif sum(head_list)>sum(mid_list):
            s= find_fake_3n(mid_list)
            return length/3+s[0],s[1]+1
        else:
            s = find_fake_3n(tail_list)
            return 2*length/3+s[0],s[1]+1


def find_fake_n(coin_list):
    n = len(coin_list)
    if n <=3:       #长度小于三时情况，递归结束条件
        if n==2:
            if coin_list[0]>coin_list[1]:
                return 1,1
            else:
                return 0,1
        else:
            s = find_fake_3(coin_list)
            return s
    else:         
        if n%3 ==0:      #能正好分成三份，比较一次，判断假币在哪堆中，递归即可
            head_list = coin_list[:n//3]
            mid_list = coin_list[n//3:2*n//3]
            tail_list = coin_list[2*n//3:]
            if sum(head_list)<sum(mid_list):
                s=find_fake_n(head_list)
                return s[0],s[1]+1
            elif sum(head_list)>sum(mid_list):
                s= find_fake_n(mid_list)
                return n/3+s[0],s[1]+1
            else:
                s = find_fake_n(tail_list)
                return 2*n/3+s[0],s[1]+1
        elif n%3 == 1:           #如果分成三份还余一个，需要再比较一次判断这一个是否为假币
            if coin_list[n-1]<coin_list[0]:
                return n-1,1
            else:         #如果多出来一个不是假币，则直接将剩下的三份比较即可，递归
                n = n-1
                s = find_fake_n(coin_list[:n])
                return s[0],s[1]+1
        elif n%3 == 2:       #如果分成三份还余2个，需要再比较一次判断这两个中是否有假币
            if coin_list[n-1]<coin_list[n-2]:
                return n-1,1
            elif coin_list[n-1]>coin_list[n-2]:
                return n-2,1
            else:           #如果多出来的2个中没有假币，则直接将剩下的三份比较即可，递归
                n = n-2
                s = find_fake_n(coin_list[:n])
                return s[0],s[1]+1
        


if __name__ == "__main__":
    print("汉诺塔问题")
    print("n=1,A转移到C  步骤:")
    Hannuota(1,'A','C') 
    print("n=4,A转移到C  步骤:")     
    Hannuota(4,'A','C')

    print("假币问题1")
    print('假设有3^5个硬币,用2代表正常硬币，第137位设为1代表假币')
    coin_list1 = []
    for i in range(3**5):
        coin_list1.append(2)
    coin_list1[137] = 1
    s = find_fake_3n(coin_list1)
    print("位置为{},寻找次数为{}".format(int(s[0]),s[1]))
    print("假币问题2")
    print('假设有1000个硬币,用2代表正常硬币，第397位设为1代表假币')
    coin_list2 = []
    for i in range(1000):
        coin_list2.append(2)
    coin_list2[397] = 1
    s = find_fake_n(coin_list2)
    print("位置为{},寻找次数为{}".format(int(s[0]),s[1]))