#lập trình các công việc
    #1.Nhập một số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại
    #2. tính tổng các chữ số của số đó
    #3. Hiển thị kết quả ra màn hình
print("Bài 3: ")
n = int(input("nhap n= "))
total = 0
while (n):
    if(n>1000):
        print("nhap lai n") 
        break
    if(n<1000):
        while (n):
            total = total + n % 10
            n = int(n / 10)

print(total)
print("")