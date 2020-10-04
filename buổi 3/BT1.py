#Bài 1: Tìm số đảo của số n
n = int(input("nhap n= "))
def daonguoc(n):
    return(str(n)[::-1])
print(daonguoc(n))
