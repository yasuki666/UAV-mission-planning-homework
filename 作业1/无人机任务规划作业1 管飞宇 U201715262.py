import math, random, statistics
import numpy as np

#1 输入三个数求最大值
def func1():
    print("输入三个数判断大小")
    number_list = []
    for i in range(3):
        number_list.append(input())
    max = number_list[0]
    for i in range(2):
        if number_list[i+1]>max:
            max = number_list[i+1]
    print(max)
    return max

#2 生成20随机浮点数并输出一系列数据
def func2():
    print("生成20个随机浮点数")
    random_number_list = []
    for i in range(20):
        random_number_list.append(random.uniform(0,100))
    print(random_number_list)
    max = random_number_list[0]
    min = random_number_list[0]
    for i in range(20):
        if random_number_list[i]>max:
            max = random_number_list[i]
        if random_number_list[i]<min:
            min = random_number_list[i]
    print("最大值为{}，最小值为{}" .format(max,min))
    mean = statistics.mean(random_number_list)
    print("平均值为{}".format(mean))
    pvariance = statistics.pvariance(random_number_list)
    print("方差为{}".format(pvariance))
    pstdev = statistics.pstdev(random_number_list)
    print("标准差为{}".format(pstdev))

#3 判断一个数是否为素数
def func3():
    print("判断一个数是否为素数,并找到1到1000内所有素数")
    def if_PrimeNumber(number):
        k=0
        for i in range(2,number):  #从3到number循环寻找因数
            if number%i==0:
                break
            k+=1
        if k==number-2:   #若无其他因数则说明是素数
            return 1
        else:
            return 0
    PrimeNumber_list = []
    for j in range(1000):
        if if_PrimeNumber(j):
            PrimeNumber_list.append(j)
    print(PrimeNumber_list)
    print("共计%d个素数" % len(PrimeNumber_list))

#4 矩阵乘法，直接调用numpy计算
def func4():
    print("矩阵乘法")
    matrix_1 = np.random.random((3, 3))  #随机生成两个3*3矩阵
    matrix_2 = np.random.random((3, 3))
    result = matrix_1.dot(matrix_2)    #点乘
    print("随机生成矩阵1：")
    print(matrix_1)
    print("随机生成矩阵2：")
    print(matrix_2)
    print("矩阵乘法结果为：")
    print(result)

#5 多无人机任务分配， 对于4飞机3任务，有一架飞机空闲，因此可以将评价矩阵改写
def func5():
    print("无人机任务分配")
    #评价矩阵
    matrix_PJ = np.array([[0,1.2,2.7,3.0],
                          [0,2.5,2.9,2.4],
                          [0,4.5,5.6,6.5],
                          [0,7.1,8.2,8.8]])
    print("PJ矩阵：")
    print((matrix_PJ))
    matrix_L = np.zeros((24, 4))
    #全排列函数
    def get_all_permu(some_list):
        if some_list:
            all_p = []
            for x in some_list:  # 第一次遍历：遍历列表中的所有元素
                temp = some_list[:]
                temp.remove(x)  # 得到不包含x的列表
                for y in get_all_permu(temp):   # 第二次遍历：遍历不包含x的所有元素的组合，开始递归
                    all_p.append([x] + y)   # 将x与不包含x的其他元素的所有组合放在一起，组成一个原列表的排列
            return all_p
        else:
            return [[]]  # 如果要排列的列表为空，则返回一个空列表
    matrix_P = get_all_permu([3, 2, 1, 0])   #对四架飞机进行全排列
    matrix_P = np.array(matrix_P)
    print("P矩阵：")
    print(matrix_P)
    for i in range(24):
        for j in range(4):
            matrix_L[i][j] = matrix_PJ[j][matrix_P[i][j]]
    print("L矩阵：")
    print(matrix_L)
    matrix_sum = np.sum(matrix_L,axis=1)    #对列求和计算sum矩阵
    print("sum矩阵：")
    print(matrix_sum)
    max_sum = np.max(matrix_sum)
    min_sum = np.min(matrix_sum)
    print("最大取值为{}，最小取值为{}".format(max_sum,min_sum))
    a = np.where(matrix_sum == max_sum)   #返回最大值索引
    print("最大价值分配方案%s"% str(matrix_P[a][0]))
    print("即第1架飞机执行%d任务\n第2架飞机执行%d任务\n第3架飞机执行%d任务\n第4架飞机执行%d任务" % (matrix_P[a][0][0],matrix_P[a][0][1],matrix_P[a][0][2],matrix_P[a][0][3]))
    b = np.where(matrix_sum == min_sum)   #返回最小值索引
    print("最小价值分配方案%s"% str(matrix_P[b][0]))
    print("即第1架飞机执行%d任务\n第2架飞机执行%d任务\n第3架飞机执行%d任务\n第4架飞机执行%d任务" % (matrix_P[b][0][0], matrix_P[b][0][1], matrix_P[b][0][2], matrix_P[b][0][3]))

if __name__ == "__main__":
    print("是否测试函数1，是：1，否：0，下同")
    s1 = input()
    if s1 == '1':
        func1()
    print("是否测试函数2")
    s2 = input()
    if s2 == '1':
        func2()
    print("是否测试函数3")
    s3 = input()
    if s3 == '1':
        func3()
    print("是否测试函数4")
    s4 = input()
    if s4 == '1':
        func4()
    print("是否测试函数5")
    s5 = input()
    if s5 == '1':
        func5()



