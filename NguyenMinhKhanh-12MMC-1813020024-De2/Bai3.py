#Đề 2
#Bài 3: Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13),
#       nếu chạy đến số 13 thì không chạy nữa (không cộng số 13) và xuất kết quả
print("Bài 3: ")
def tinh_tong(s):
    tong = 0
    for i in range (0,s):
        if (i == 13 ):
            break
        else:
            tong += i
        
    return tong
if __name__ == "__main__":
    s=int(input("nhap s= "))
    print("Tổng các giá tri từ 1 đến ",s," là: ",tinh_tong(s))