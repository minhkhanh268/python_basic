#in ra bảng cửu chương n 
n= int(input("nhap n= "))
def bangcuuchuong(n):

    for j in range(1,10):
        s = n * j
        print(n, "*" ,j, "=" ,s)
    
print("bảng cửu chương",n)
bangcuuchuong(n)