'''
#W5A1
def Max_Of_Two(a, b) -> int:
    if a > b:
        return a
    else:
        return b
a, b = map(int, input().split())
print(Max_Of_Two(a, b))
#W5A2
def swap(a, b):
    return b, a
a, b = map(int, input().split())
print(swap(a, b))
#W5A3
def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n=int(input())
print(so_nguyen_to(n))
#W5A4
def so_hoan_hao(n):
    if n < 1:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
n=int(input())
print(so_hoan_hao(n))
#W5A5
def vi_tri(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1
a = list(map(int, input().split()))
k = int(input())
print(vi_tri(a, k))
#W5A6
def tinh_giai_thua(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input())
print(tinh_giai_thua(n))
#W5A7
def may_tinh_bo_tui(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
a, opertor, b = input().split()
a = int(a)
b = int(b)
print(may_tinh_bo_tui(a, b, opertor))
#W5A8
def hamming(a, b):
    return bin(a ^ b).count('1')
a, b = map(int, input().split())
print(hamming(a, b))

#W5A9
def tong_cac_chu_so(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
n = int(input())
print(tong_cac_chu_so(n))
#W5A10
X, Y = input().split()
def mapping(X, Y):
    A = list(X)
    B = list(Y)

    n = len(A)
    M = [True]*n

    for i in range (n):
        temp = A[i]
        for j in range (n):
            if M[j] and A[j] == temp:
                A[j] = B[i]
                M[j] = False
    return A == B
if mapping(X, Y) and mapping(Y, X):
    print("true")
else:
    print("false")
'''
