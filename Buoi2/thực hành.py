#1. Xuất ra màn hình N lần câu thông báo "Hello Python"
print("Bài 1: ")
n=int(input('Nhap n: '))
for n in range(0,n,1):
    print("Hello Python")
print("")

#2. Tính tổng từ 1 cho đến N
print("Bài 2: ")
n =int(input('Nhập N: '))
sum = 0
for i in range(1,n+1):
    sum += i   
print(f"Tổng từ 1 cho đến N là: {sum}")
print("")

#3. tính tổng các số chẳn nằm trong từ 0 đến N
print("Bài 3: ")
n=int(input('Nhập n: '))
chan=0
for i in range (0,n+1):
    if(i % 2 ==  0):
            chan += i
            print (i)
    #else
print(f"Tổng các số chẳn nằm trong từ 0 đến N là: {chan}")
print("")
#4. Tính tổng các số lẽ nằm trong đọn từ 0 đến N
print("Bài 4: ")
n =int(input('nhap n= '))
le=0
for i in range (0,n+1):
    if(i % 2 !=0 ):
        le +=i
        print (i)
    else:
        print()
print("tong cac so le ", le)
print("")
#5.	Tính trung bình cộng các số trong mảng
print("Bài 5: ")
n = int(input('nhap n= '))
tong=0
i=1
tongtrungbinh = int
for i in range(i,n+1):
    tong +=i
    print (tong)
tongtrungbinh = tong / n
print("tong trung binh cong trong mang ", tongtrungbinh)
print("")
#6.	Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
print("Bài 6: ")
n = int(input('nhap n= '))
tong = 0
for i in range (1,n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)
print("")
#7.	Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
print("Bài 7: ")
n= int(input('nhap n= '))
tong= 0
for i in range (1,n+1):
    if(i == 17):
        continue
         
    else:
        tong += i
        print(i, tong)
print (tong)
print("")
