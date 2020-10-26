#Đề 2
#Bài 2: Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong
#       năm. Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
print("Bài 2: ")
def mua(n):
    if ( n == 1 or n <= 3):
        return("Xuân")
    elif (n == 4 or n <= 6):
        return("Hạ")
    elif ( n == 7 or n <= 9):
        return("Thu")
    elif ( n == 10 or n <=12):
        return("Đông")
    else:
        return("Tháng không hợp lệ")
if __name__ == "__main__":
    n=int(input("nhap n= "))
    print(mua(n))