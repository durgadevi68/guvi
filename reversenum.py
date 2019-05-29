r=int(input())
sum=0
while(r!=0):
  b=r%10
  sum=sum*10+b
  r=r//10
print(sum)
