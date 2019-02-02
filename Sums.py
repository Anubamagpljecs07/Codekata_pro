n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]+l[j])==m:
            s+=1
            continue
if s>0:
    print("yes")
else:
    print("no")
