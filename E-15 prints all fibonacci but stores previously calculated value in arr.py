def fib(n,memo):
    if n<=0: return 0
    if n==1: return 1
    elif memo[n]>0: return memo[n] 
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    # print(memo,memo[n])
    return memo[n]

def allfib(n):
    memo = [0]*(n+1)
    for i in range(1,n+1):
        print(i," : ",fib(i,memo))

allfib(10)