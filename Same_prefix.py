n=int(input())
l,m=[],[]
for i in range(0,n):
	l.append(input())
for i in l:
	m.append(len(i))
n=min(m)
g=l[0][0:n]
a=""
c=0
for i in range(1,len(l)):
	for j in range(0,n):
		if c==0:
			if g[j]==l[i][j]:
				a=a+g[j]
			else:
				break
print(a)
