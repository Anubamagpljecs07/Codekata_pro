s,r=map(str,input().split())
c=0
for i in range(0,len(s)):
    for j in range(0,len(r)):
        if s[i:i+2]==r[j:j+2]:
            c+=1
if c==0:
    print("no")
else:
    print("yes")

