#tính tổng các số nguyên tố
def songuyento(n):
    count = 0
    s =0 
    for i in range(1, n + 1):
        if n % i == 0:
            s=s+i
            count += 1
    if count == 2:
        return s
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print("tong cac so nguyen to la: ",songuyento(n))
