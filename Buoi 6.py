#W6A1
a = list(map(int, input().split()))
b = [a[0]]
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        b.append(a[i+1])
print(b)
#W6A2
a = list(map(int, input().split()))
b = []
sum = 0
for i in a:
    sum += i
    b.append(sum)
print(b)
#W6A3
a = tuple(map(int, input().split()))
b = []
k = int(input())
if k > len(a):
    print(a)
else:
    b = a[k:] + a[:k]
    print(tuple(b))
#W6A4
a = map(str, input().split())
b = {}
for i in a:
    x, y = i.split(':')
    if x not in b:
        b[x] = [int(y)]
    else:
        b[x].append(int(y))
print(b)
#W6A5
a = list(map(int, input().split()))
b = {'positives': 0, 'negatives': 0, 'zeros': 0}
for i in a:
    if i > 0:
        b['positives'] += 1
    elif i < 0:
        b['negatives'] += 1
    else:
        b['zeros'] += 1
print(b)
#W6A6
a = list(map(int, input().split()))
sum = 0
for i in a:
    sum += i
print(sum)
#W6A7
a = tuple(map(int, input(). split()))
x = len(a) - 1
b = []
for i in range(len(a)):
    b.insert(0, a[i])
print(a[0], a[x], tuple(b))
#W6A8
a = list(map(str, input().split()))
b = {}
for i in range(len(a)):
    if a[i] not in b:
        b[a[i]] = 1
    else:
        b[a[i]] += 1
print(b)
#W6A9
dic1 = eval(input())
dic2 = eval(input())
for key, value in dic2.item:
    if key in dic1:
        dic1[key] += value
    else:
        dic1[key] = value
print(dic1)
#W6A10
a = list(map(int, input().split()))
k = int(input())
b = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            b.append((a[i], a[j]))
print(sorted(b))
#W6A11
a = tuple(map(int, input().split()))
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    elif i % 2 !=0:
        c.append(i)
print(tuple(b))
print(tuple(c))
#W6A12
a = list(map(int, input().split()))
b = 0
count = 0
sum = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            sum += 1
    if sum > count:
        count = sum
        b = a[i]
    if sum == count:
        if b > a[i]:
            b = a[i]
    sum = 0
print(b)
#W6A13
a = input().split()
b = {}
for i in range(len(a),2):
    b[i] = i + 1
for key, value in enumerate(a):
    if value not in b:a
        b[value] = [key]
    else:
        b[value].append(key)
print(b)

