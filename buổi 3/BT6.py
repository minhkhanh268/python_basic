#xem 1 số có phải là số nguyên tố hay không
def songuyento(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "là số nguyên tố"
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print(songuyento(n))
