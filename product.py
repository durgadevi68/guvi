a=int(input())
product=1
k=0
while(a):
    k=a%10
    product=product*k
    a=a//10
print(product)
