n=int(input())
l=list(map(int,input().split()))
g=[]
c=1
for i in range(0,len(l)):
	if i<=len(l)-1 and i>1:
		if l[i]>l[i-1]:
			c+=1
		elif l[i]<=l[i-1]:
			g.append(c)
			c=1
		if i==len(l)-1:
			g.append(c)
	if i==0:
		if l[i]<l[i+1]:
			c+=1
			if len(l)==2:
				g.append(c)
		else:
			g.append(c)
a=max(g)
if a<2:
	a=a-2
print(a)
