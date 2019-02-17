s=input()
r=input()
s=list(s.split("|"))
if len(s[0])==len(s[1]):
    print("Impossible")
elif len(s[1])+len(r)==len(s[0]):
    g=""
    s[1]=s[1]+r
    g=g+s[0]+"|"+s[1]
    print(g)
else:
    print("Impossible")
