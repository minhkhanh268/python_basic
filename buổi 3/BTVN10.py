import math
n=int(input("nhap n= "))
def tongcacsole(n):
    s=0
    count=0
    while (n):
        s =  n % 10
        if(s % 2 != 0):
            count=count + 1
        n = int(n / 10)
    print("so luong so le la: ",count)
tongcacsole(n)
