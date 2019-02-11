k=int(input())
g=[]
for i in range(0,k):
    g.append(list(map(int,input().split())))
h=sorted(g)
f=[]
for i in h:
    for j in i:
        f.append(j)
print(*f)
