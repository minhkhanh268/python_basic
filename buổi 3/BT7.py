#xem một số có phải là số chính phương hay không
import math
n=int(input("nhap n= "))
x = math.sqrt(n)
s=0
def sochingphuong(n):
    if(x * x == n):
            
        return "là số chính phương"
    else:
        return  "không phải là số chính phương"
print(n,sochingphuong(n))