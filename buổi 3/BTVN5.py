def count_upper_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
    print("Cau tu da nhap la: ",s)
    print("So chu in hoa: ", count_upper)
    print("So chu in thuong: ", count_lower)


s = str(input('Viet 1 cau tu: '))
count_upper_lower(s)