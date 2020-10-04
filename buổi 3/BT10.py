#tính số fibo thứ n
def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input("nhap n = "))
print(fibonacci(n))