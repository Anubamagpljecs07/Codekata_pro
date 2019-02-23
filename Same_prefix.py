n=int(input())
l,m=[],[]
for i in range(0,n):
	l.append(input())
for i in l:
	m.append(len(i))
n=min(m)
g=l[0][0:n]
g=list(g)
a=""
c=0
for i in range(1,len(l)):
	for j in range(0,n):
		if c==0:
			if g[j]!=l[i][j]:
				g[j]=""
			
for i in g:
	a=a+i
print(a)
