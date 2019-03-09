n=int(input())
l=list(map(int,input().split()))
l=sorted(l,reverse=True)
A,B=0,0
g=0
for i in l:
	g=A+i
	if B>g:
		A=g
	else:
		A=B
		B=g
print(A,B)
