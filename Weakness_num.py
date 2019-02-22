n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	for j in range(0,len(l)):
		for k in range(0,len(l)):
			if i<j<k and l[i]>l[j]>l[k]:
				c+=1
print(c)
