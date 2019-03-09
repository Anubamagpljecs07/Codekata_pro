n1=input()
n=n1[::-1]
n1=list(n1)
c=0
for i in range(0,len(n)):
	if n[i]=='0':
		c+=1
	else:
		break
for i in range(0,c):
	n1.insert(0,"0")
if n1==n1[::-1]:
	print("yes")
else:
	print("no")
