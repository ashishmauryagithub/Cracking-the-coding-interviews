#Ttime complexity of the program is O(2^n)
def fib(n):
    if n<=0: return 0
    if n==1: return 1
    return fib(n-1)+fib(n-2)
def allfib(n):
    for i in range(n):
        print(i," : ",fib(i))

allfib(4)
