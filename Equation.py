n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in range(0,len(l)):
	for j in range(0,len(l)):
		for k in range(0,len(l)):
			if i<=j<=k:
				f=p*l[i]+q*l[j]+r*l[k]
				g.append(f)
print(max(g))
