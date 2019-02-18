a=input()
g=""
l=[]
f=[]
for i in range(0,len(a)):
    if a[i] not in g:
        g=g+a[i]
    elif a[i] in g :
        l.append(g)
        f.append(len(g))
        g=""
    if i==len(a)-1:
        l.append(g)
        f.append(len(g))
        g=""
    
for i in l:
    if len(i)==max(f):
        print(i)
