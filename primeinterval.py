a,b= input().split()
x=int(a)
y=int(b)
for i in range(x + 1 , y ):
   s=0
   for j in range(2,i):
      if((i%j)==0):
        s=1
        break
      else:
        continue
   if(s==0):
      print(i, end=" ")
  
