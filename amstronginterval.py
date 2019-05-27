a,b= input().split()
x=int(a)
y=int(b)
for i in range(x + 1 , y ):
  i=str(i)
  s=0
  for j in range (0,len(i)):
      s=s+(int(i[j])**3)
  if(int(i)==s):
      print(s, end=" ")
  
