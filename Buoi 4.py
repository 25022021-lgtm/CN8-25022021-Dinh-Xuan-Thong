'''
#SumOfNumbers
n = int(input("Nhap so nguyen duong n: "))
if n <= 1000 and n > 0:
    tong = 0
    for i in range(1,n + 1):
        tong += i
    print("Tong cua",n,"so nguyen duong dau tien la:",tong)
else:
    print("Vui long nhap so nguyen duong n nho hon hoac bang 1000")
#PrimeNumberCheck
n = int(input("Nhap so nguyen duong n: "))
if n > 1:
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            print(n,"khong phai la so nguyen to")
            break
    else:
        print(n,"la so nguyen to")
#FactorialCalculation
n = int(input("Nhap so nguyen duong n: "))
if n > 0 and n < 100:
    giai_thua = 1
    for i in range(1,n + 1):
        giai_thua *= i
    print("Giai thua cua",n,"la:",giai_thua)
else:
    print("Vui long nhap so nguyen duong n nho hon 100")
#CountingDigits
n = int(input("Nhap so nguyen n: "))
if n < 0:
    dem = 0
    n = abs(n)
    while n > 0:
        dem += 1
        n //= 10
elif n > 0:
    dem = 0
    while n > 0:
        dem += 1
        n //= 10
else:
    dem = 1
print("So chu so cua n la:",dem)
#MeaningOfLife
n = int(input("Nhap so nguyen n: "))
x = map(int, input("Nhap so nguyen x: ").split())
for i in x:
    if i == 42:
        print("I 've found the meaning of life!")
        break
else:
    print("It's a joke!")
#SumPrimeInRange
a, b = map(int, input("Nhap hai so nguyen a va b: ").split())
tong = 0
for num in range(a, b + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            tong += num
print("Tong cac so nguyen to trong khoang tu",a,"den",b,"la:",tong)
#LargestPrimeFactor
n = int(input("Nhap so nguyen n: "))
max_prime = -1
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        max_prime = i
        n //= i
if n > 1:
    max_prime = n
print("Uoc so nguyen to lon nhat cua n la:",max_prime)
#ReverseAddPalindrome
def palindrome(num):
    return str(num) == str(num)[::-1]
n = int(input("Nhap so nguyen n: "))
count = 0
while not palindrome(n):
    n += int(str(n)[::-1])
    count += 1
print("So buoc de bien n thanh so doi xung la:",count)
print("So doi xung thu duoc la:",n)
#W4A9
n = int(input())
a = []
for i in range(1, n+1):
    if i ** 0.5 == int(i ** 0.5):
        a.append(i)
print(*a)
#W4A12
a, b = map(int, input().split())
print(int(a*(1.007**b)))
#W4A11
n = int(input())
count = 0
for i in range(2, (n+1)/2):
    if n % i == 0 and i % 2 == 0:
        count += 1
print(count)
#W4A13
def close_pair(a, b):
    sum = 1
    for i in range(2, int(a/2+1)):
        if a % i == 0:
            sum += i
    if sum == b:
        return True
    else:
        return False
x, y = map(int,input().split())
if close_pair(x,y) and close_pair(y,x):
    print("true")
else:
    print("false")
#W4A14
def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(gcd(a, b))
#W4A20
n = int(input())
while n % 2 == 0:
    n //= 2
if n == 1:
    print("true")
else:
    print("false")
#W4A23
n = int(input())
S = 0
while S < n:
    for k in range(1, n):
        S += k
        if S >= n:
            print(k)
            break
#W4A24
def check_password(password):
    if len(password) <= 6:
        return False
    
    has_upper = False   
    has_lower = False   
    has_digit = False   
    has_special = False 
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False
s = input()
if check_password(s):
    print("true")
else:
    print("false")
#W4A34
a = input()
b = input()
c = a.split(b)
print(''.join(c))
'''

