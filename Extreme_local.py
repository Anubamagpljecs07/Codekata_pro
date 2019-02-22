n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
	if i>0 and i<len(a)-1:
		if a[i]<a[i+1] and a[i]<a[i-1]:
			c+=1
		elif a[i]>a[i+1] and a[i]>a[ai-1]:
			c+=1
print(c)
