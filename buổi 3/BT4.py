#tính tổng các số lẻ
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 != 0):
            
            s+=i
    return s

n=int(input("nhap n= "))
print("tong cac so le ",tong(n))




        
