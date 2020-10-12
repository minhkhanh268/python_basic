print('Bài tập 01: Viết chương trình nhập xuất mảng 1 chiều (List )')
print('a. Tính tổng của mảng 1 chiều')
a = int(input("nhập giá trị a="))
def tong(a):
    arr = [] 
    tong = 0 
    for s in range (a):
        o = input(f"nhập vào 1 giá trị[{s}]: ")
        arr.append(int(o))
        tong+=arr[s]
    return tong
print("tổng các phần tử trong mảng 1 chiều: ",tong(a))
print('b.Tích của mảng 1 chiều')
def tich(a):
    arr = [] 
    tich = 1
    for x in range (a):
        t = input(f"nhập vào giá trị[{x}]: ")
        arr.append(int(t))
        tich*=arr[x]
    return tich
print("Tích của các phần tử trong mảng 1 chiều : ",tich(a))
print(" c. Tìm giá trị lớn nhất")
def max(a):
    arr = []
    
    for y in range (a):
        s = input(f"nhập vào giá trị của mảng [{y}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > m):
            m=arr[i]
    return m
print("số lớn nhất tìm được trong mảng là: ",max(a))
print(" c. Tìm giá trị nhỏ nhất")
def min(a):
    arr = []
    
    for z in range (a):
        s = input(f"nhập vào giá trị của mảng [{z}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[t] < m):
            m=arr[t]
    return m
print("số nhỏ nhất tìm được trong mảng là: ",min(a))
print("e.tìm các số lẻ trong mảng")
def so_le(a):
    result = []
    arr = []
    
    for s in range (a):
        o = input(f"nhập vào giá trị của mảng[{s}]: ")
        arr.append(int(o))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 != 0 ):
            result.append(arr[s])
    return result
print("các số lẻ cần tìm trong mảng là : ",so_le(a))
print('f.tìm số chẵn trong mảng')
def so_chan(a):
    result = []
    arr = []
    
    for s in range (a):
        y = input(f"nhập vào giá trị cần tìm trong mảng[{s}]: ")
        arr.append(int(y))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 == 0 ):
            result.append(arr[s])
    return result
print("các số chẵn cần tìm trong mảng là: ",so_chan(a))
print("bài 3 trên zalo")
list1=[4,5,6]
arr= []
a = int(input("nhập vào giá trị a= "))
for s in range (a):
    i = input(f"nhập vào 1 giá trị[{s}]: ")
    arr.append(int(i))
print(arr)
print(list1)
print(list1 + arr)
print("bài 2 trong pdf")
a =int(input("input a value= "))
def timidbaihat(a):
    result =[]
    arr = []
    count =0
    
    for s in range (a):
        i = input(f"input random value[{s}]: ")
        arr.append(int(i))
    for s in arr:
        if s not in result:
            result.append(s)
            count+=1
    return count,result
print(timidbaihat(a))