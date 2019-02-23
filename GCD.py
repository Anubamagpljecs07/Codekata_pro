def gcd(m,n):
	x=[]
	for i in range(1,max(m,n)):
		if m%i==0 and n%i==0:
			x.append(i)
	n=max(x)
	return n
n,k=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in range(0,k):
	l,r=map(int,input().split())
	f=l,r
	g.append(f)
for i in g:
	if i[0]!=i[1]:
		for j in range(i[0]+1,i[1]+1):
			d=gcd(l[j],l[j+1])
