n,a,b=map(int,input().split())
m=n//2
c=0
if n%2==1:
	print("NO")
else:
	for i in range(1,m+1):
		for j in range(1,m+1):
			if i*a==m:
				print("YES")
				c+=1
				break
			elif i*b==n:
				print("YES")
				c+=1
				break
			elif i*a + j*b==m:
				print("YES")
				c+=1
				break
		if c>=1:
			break
		
