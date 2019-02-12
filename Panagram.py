l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=input()
g=[]
for i in s:
    if i.upper() not in g and i.isalpha():
        g.append(i.upper())
c=0
for i in g:
    if i in l:
        c+=1
if c==26:
    print("yes")
else:
    print("no")
