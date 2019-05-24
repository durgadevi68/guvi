n=input()
n=n.split()
N=int(n[0])
K=int(n[1])
k=input()
k=k.split()
sum=0
for i in range(K):
  sum=sum+int(k[i])
print(sum)
