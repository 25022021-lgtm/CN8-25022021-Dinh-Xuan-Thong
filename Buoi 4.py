#SumOfNumbers
n=int(input("Nhap so nguyen duong n: "))
if n<=1000:
    tong=0
    for i in range(1,n+1):
        tong+=i
    print("Tong cua",n,"so nguyen duong dau tien la:",tong)
else:
    print("Vui long nhap so nguyen duong n nho hon hoac bang 1000")