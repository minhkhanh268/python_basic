#tính tổng 1^3+2^3+...n^3
n = int(input("nhap n= "))
def tong(n):
    s=0
    for i in range (1,n+1):
        s= s + pow(i,3)
    return s
print ("tong la ",tong(n))