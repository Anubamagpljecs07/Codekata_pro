n=int(input())
l=list(map(int,input().split()))
g=[]
s=[]
f=[]
l=sorted(l,reverse=True)
for i in l:
    g.append(str(bin(i)))
for i in g:
    s.append(i.count('1'))
a=sorted(s,reverse=True)
for i in a:
    for j in g:
        if str(j).count('1')==i:
            f.append(j)
anu=[]
for i in f:
    for j in l:
        if bin(j)==i and j not in anu:
            anu.append(j)
for i in anu:
    print(i)
