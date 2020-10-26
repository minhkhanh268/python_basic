#Đề 2
#Bài 4: Giả sử có một chuỗi như sau: “0983876207;0918295063;0002;05:18:25;”, tách chuỗi
#       trên thành từng phần riêng biệt
print("Bài 4: ")
def tinhtiendienthoai(chuoi):
    
    chuoi1 = chuoi.split(";")
    tg = chuoi1[3].split(":")
    tong_so_phut = float(tg[0]) * 60 + float(tg[1]) + float(tg[2]) / 60
    money = tong_so_phut * 2500
    return int(money)
if __name__ == "__main__":
    chuoi=str("0983876207;0918295063;0002;05:18:25")
    print("Ta có chuỗi:", chuoi)
    print("tính giá cước trên là: ",tinhtiendienthoai(chuoi))