n=int(input())
s=list(map(int,input().split()))
s=sorted(s)
c=0
for i in range(0,len(s)):
	k=0
	g=s[i+1::]
	print(g)
	for j in g:
		k+=int(j)
	if k<=i:
		c+=1
print(c)
