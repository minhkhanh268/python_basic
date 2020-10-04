#tính n!
n = int(input("nhap n= "))
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thua của ",n," là ",tinhgiaithua(n))