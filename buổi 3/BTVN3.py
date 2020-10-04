#bài 3
n=int(input("nhap n="))
def is_perfect(n):
    Tong=0
    for i in range (1,n):
        if n % i == 0:
            Tong=Tong+i
    if Tong==n:
        return "là số hoàn hảo"
    else:
        return "không phải là số hoàn hảo"
print(n,is_perfect(n))