n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
	for j in range(len(l)):
		for k in range(len(l)):
			if i<j<k and l[i]<l[j]<l[k]:
				c+=1
print(c)
