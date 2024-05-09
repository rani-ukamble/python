# Generators: way of creating iterators
def remote_control_next():
    yield "cnn"
    yield "ysn"

itr = remote_control_next()
# print(itr)
# print(next(itr))
# print(next(itr))


# for c in remote_control_next():
#     print(c)
  
  

#fib series  1 

# def fib(n):
#     if n<2:
#         return 
#     return fib(n-1)+fib(n-2)
# for i in range(10):  
#        print(fib(i))
       

#fib series 2     
# def fibo(n):
#     n1, n2 = 0, 1
#     cnt = 0    
#     while cnt<n:
#         print(n1, end=" ")
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         cnt +=1       
# fibo(10)  


#fib series using generator 1
def fibonacci():
    n1, n2 =0, 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2
# Invoking the generator and printing Fibonacci numbers up to 50
fib = fibonacci()
while True:
    f = next(fib)
    if f > 50:
        break
    print(f)
    