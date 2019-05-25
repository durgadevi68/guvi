x=input()
a=x.split()
n=int(a[0])
k=int(a[1])
y=input()
b=y.split()
d=[]
j=1
for i in range (0,n):
    z=int(b[i])
    if ((z%2)!=0):
        d.append(b[i])
while(j!=k):
    j+=1
print(d[j-1])
