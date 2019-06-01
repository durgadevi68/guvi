a=input()
b=int(a)
l=[]
for i in range(0,b):
    d=input()
    l.append(d)
P=[]    
for i in zip(*l):
    if(i.count(i[0])==len(i)):
        P.append(i[0])
    else:
        break
print(''.join(P))
