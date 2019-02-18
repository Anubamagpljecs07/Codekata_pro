a=input()
g=""
f=[]
for i in range(0,len(a)):
    if a[i] not in g:
        g=g+a[i]
    elif a[i] in g :
        f.append(len(g))
        g=""
    if i==len(a)-1:
        f.append(len(g))
        g=""
    
print(max(f))
