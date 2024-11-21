def fib(n):
    n1=0
    n2=1
    series=[]
    for _ in range(n):
        series.append(n1)
        n1,n2=n2,n1+n2
       
    return series
number=int(input("Enter the number : "))
print("Fibonacci Series: ",fib(number))
