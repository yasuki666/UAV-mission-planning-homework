import random


def quick_sort(input_list, left, right):#快速排序
    if left >= right:  
        return

    mid = input_list[left]  # 设定基准数
    i = left  
    j = right  
    while i < j:
        while i < j and input_list[j] >= mid:
            j -= 1
        input_list[i] = input_list[j] 
        while i< j and input_list[i] < mid:
            i += 1
        input_list[j] = input_list[i]  
    # 退出循环后，i与j重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    input_list[i] = mid  
    quick_sort(input_list, left, i - 1)  #左右子数列递归
    quick_sort(input_list, i + 1, right) 

def merge(a_list,b_list):   #先定义归并函数
    c_list = []
    i=j=0
    while i<len(a_list) and j<len(b_list): #将两个子数列中较大的数填入主数列 
        if a_list[i] < b_list[j]:
            c_list.append(a_list[i])
            i +=1
        else:
            c_list.append(b_list[j])
            j +=1

    if i==len(a_list):     #任一子数列到底，直接将另一数列剩下的数填入
        for k in b_list[j:]:
            c_list.append(k)
    else:
        for k in a_list[i:]:
            c_list.append(k)    
    return c_list

def merge_sort(input_list): #归并排序函数
    if len(input_list) <= 1:
        return input_list
    mid = int(len(input_list)/2)   #二分
    list1 = input_list[0:mid]
    list2 = input_list[mid:]
    list1 = merge_sort(list1)   #两个子数列递归
    list2 = merge_sort(list2)
    return merge(list1,list2)

def main():
    test_list1 = []
    for i in range(100):
        test_list1.append(random.randint(0,100))
    print("随机生成数组")
    print(test_list1)
    quick_sort(test_list1, 0, len(test_list1) - 1)
    print("快速排序之后")
    print(test_list1)
    test_list2 = []
    for i in range(100):
        test_list2.append(random.randint(100,200))
    print("随机生成数组")
    print(test_list2)
    test_list2 = merge_sort(test_list2)
    print("归并排序之后")
    print(test_list2)

if __name__ == '__main__':
    main()

