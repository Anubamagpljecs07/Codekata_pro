#ganu
n=int(input())
l=list(map(int,input().split()))
g=[]
for j in range(n):
	if len(l)!=0:
		m=min(l)
		a=l.count(m)
		g.append(a)
		for i in range(0,a):
			l.remove(m)
f=0
j=1
for i in g:
	f=f+(i*j)
	j+=1
print(f)
	
