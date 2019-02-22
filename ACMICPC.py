n,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in l:
	if i<=(5-k):
		d+=1
g=d//3
print(g)
