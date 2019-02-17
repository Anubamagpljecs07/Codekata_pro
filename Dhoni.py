s="dhoni"
m=input()
c=0
for i in m:
    if m.count(i)==s.count(i):
                c+=1
if c==len(m):
    print("yes")
else:
    print("no")
