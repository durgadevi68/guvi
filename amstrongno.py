a=input()
s=0
for i in range (0,len(a)):
        s=s+(int(a[i])**3)
s=str(s)
if(a==s):
        print("yes")
else:
        print("no")
