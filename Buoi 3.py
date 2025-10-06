#Nhap so de dao nguoc so
n = int(input())
n = str(n)[::-1]
n = int(n)
print(n)
#Hoan doi 2 so
a, b = map(int, input().split())
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
#Kiem tra mot so co phai la luy thua cua 2
n = int(input())
if (n & (n - 1)) == 0:
    print("True")
else:
    print("False")
#Chia m cho n lay phan nguyen lam tron xuong
m, n = map(int, input().split())
print(m // n)
#Chia m cho n lam tron len
m, n = map(int, input().split())
if m % n == 0:
    print (m // n)
else:
    print(m // n + 1)

#Kiem tra chan le
x=int(input())
if x%2==0:
    print("Even")
else:
    print("Odd")
#Kiem tra 2 so cung am
a=int(input())
b=int(input())
if a<0 and b<0:
    print("Yes")
else:
    print("No")
#Nhap vao 2 chuoi a va b neu a dai hon b thi in ra True nguoc lai in ra False
a=str(input())
b=str(input())
if len(a)>len(b):
    print("True")   
else:
    print("False")
#Nhap vao 3 so a,b,c kiem tra xem co phai la 3 canh cua tam giac khong
a=int(input())
b=int(input())
c=int(input())
if a+b>=c and a+c>=b and b+c>=a:
    print("Yes")
else:
    print("No")