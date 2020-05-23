import time
def Fibonacci(n):
    if n<2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
fib_memo = {}
def Fibonacci_preserved(n):
    if n < 2: return 1
    if not n in fib_memo:
        fib_memo[n] = Fibonacci_preserved(n-1) + Fibonacci_preserved(n-2)
    return fib_memo[n]

if __name__ == "__main__":
    start_time = time.time()
    print(Fibonacci(35))
    end_time = time.time()
    print("{}s".format(end_time-start_time))

    start_time = time.time()
    print(Fibonacci_preserved(35))
    end_time = time.time()
    print("{}s".format(end_time-start_time))