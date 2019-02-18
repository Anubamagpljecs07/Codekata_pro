a,b=map(str,input().split())
g=""
for i in range(0,len(a)):
	g=g+chr(97+(ord(a[i])+ord(b[i])-97-97+1)%26)
print(g)
