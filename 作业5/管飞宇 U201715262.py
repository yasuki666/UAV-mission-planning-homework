#切割钢条问题
best_list = {}
def find_max(n,money_list):   #求对于长度为n钢条的最优切割价钱
    if not n-1 in best_list:        #如果之前没储存过子问题最优解
        if n == 1:
            best_list[n-1] = money_list[0]
        else:                     #若n!=1，由动态规划拆分成n,(n-1)+1.(n-2)+2………………n/2+n/2,比较哪种方案最优
            s = [money_list[n-1]]               #不切割的价钱
            for i in range(n//2):
                i += 1 
                s.append(find_max(n-i,money_list)+find_max(i,money_list))           #各种局部最优切割方案的价钱列表
            max = s[0]
            for i in s:
                if i>max:
                    max = i                    #比较得到整体最优方案
            best_list[n-1] = max             #把得到的最优解储存起来
    return best_list[n-1]                #返回已储存的最优解
def cutting_bar(input_list):
    for i in range(len(input_list)):
        print("r{}={}".format(i+1,find_max(i+1,input_list)),end = " ")


#附加题 输出具体的最优方案
best_plan_list = {}
def find_max_plan(n,money_list):
    if not n-1  in best_plan_list:   #如果之前没储存过子问题最优解
        if n == 1:                    #递归结束条件
            best_plan_list[n-1] = [1] 
        else:
            k = [n]              #不切割时候的方案
            max = money_list[n-1]
            for i in range(n//2):           #遍历各种局部最优切割方案，如果好于现有方案则替代，直到最后找到整体最优方案
                i +=1
                if find_max(n-i,money_list)+find_max(i,money_list)>max:
                    max = find_max(n-i,money_list)+find_max(i,money_list)
                    k = find_max_plan(n-i,money_list) + find_max_plan(i,money_list)
            best_plan_list[n-1] = k      #把得到的最优解储存起来
    return best_plan_list[n-1]         #返回已储存的最优解



def cutting_bar_plan(input_list):
     for i in range(len(input_list)):
        print("r{}={},切割方案:{}".format(i+1,find_max(i+1,input_list),find_max_plan(i+1,input_list)))


#无人机执行任务最多问题
def max_task_by_earliest_endtime(s_list,f_list):
    task_list = []
    now_time = 0
    for j in range(len(s_list)):            #最多不过执行n次任务，可以改成while(now_time>max(s_list))
        k = 0
        earlist_end_time = 100          #起始大数，不能小于max(f_list)
        for i in range(len(s_list)):
            if s_list[i]>=now_time:
                if f_list[i]<earlist_end_time:       #如果此任务开始时间晚于上一次任务结束时间且结束时间最早，即得到局部最优
                    earlist_end_time = f_list[i]
                    k=i+1
        if k != 0:
            task_list.append(k)         #记录每次遍历得到的局部最优解，得到整体最优解
        now_time = earlist_end_time   #记录上次任务结束时间，用于寻找下一个任务
    return task_list


def max_task_by_latest_starttime(s_list,f_list):
    task_list = []
    now_time = 100              #起始大数，不能小于max(f_list)
    for j in range(len(s_list)):    #最多不过执行n次任务，可以改成while(now_time>max(s_list))
        k = 0
        latest_start_time = 0
        for i in range(len(s_list)):
            if f_list[i]<=now_time:
                if s_list[i]>latest_start_time:    #如果此任务结束时间早于上一次任务开始时间且开始时间最晚，即得到局部最优
                    latest_start_time = s_list[i]
                    k = i+1
        if k !=0:
            task_list.append(k)      #记录每次遍历得到的局部最优解，得到整体最优解
        now_time = latest_start_time            #记录上次任务开始时间，用于寻找下一个任务
    return task_list


if __name__ == "__main__":

    given_list = [1,5,8,9,10,17,17,20,24,30]
    print("钢条切割问题")
    cutting_bar(given_list)
    print("\n附加题，输出具体切割方案")
    cutting_bar_plan(given_list)
    
    s = [5,6,8,8,2,12,1,3,0,5,3]
    f = [9,10,11,12,14,15,4,5,6,7,9]
    print('\n无人机执行任务最多问题')
    print('贪心算法，每次结束最早')
    print(max_task_by_earliest_endtime(s,f))
    print('附加题，每次开始最晚')
    print(max_task_by_latest_starttime(s,f))





