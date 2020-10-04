#Bai tap 1: Max and Min
print('**********************************')
print('Bai tap 1: Max_Min')
b=int(input('Nhap 1 so B bat ki: '))
a=[3,4,1,8,23,16,18,98,b]
lon = 0
nho = b
for i in a:
    if i < nho:
        nho=i
for i in a:
    if i > lon:
        lon=i
print(lon,' La so Max')
print(nho,' La so Min')