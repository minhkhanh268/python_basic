#Lập trình thực hiện các công việc sau: 
    #1. Nhập 3 số a,b,c bất kì
    #2. Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    #nếu đúng là tam giác thì xác định tam giác vuông hay không?
print("Bài 4: ")
a=int(input("nhap a= "))
b=int(input("nhap b= "))
c=int(input("nhap c= "))
if( (a<b+c)&(b<a+c)&(c<a+b) ):
    if( (a*a==b*b+c*c) | (b*b==a*a+c*c) | (c*c== a*a+b*b)):
        print("đây là hình tam giác vuông")
    else:
       print("đây là hình tam giác nhưng không phải là hình tam giác vuông")
else:
    print("đây không phải hình tam giác")
print("")