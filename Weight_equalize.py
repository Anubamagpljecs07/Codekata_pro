s=input()
r=input()
s=list(s.split("|"))
if len(s[0])==len(s[1]):
    print("Impossible")
if len(s[1])<len(s[0]):
    if len(s[1])+len(r)==len(s[0]):
        g=""
        s[1]=s[1]+r
        g=g+s[0]+"|"+s[1]
        print(g)
    else:
        print("Impossible")
if len(s[0])<len(s[1]):
    if len(s[0])+len(r)==len(s[1]):
        g=""
        s[0]=s[0]+r
        g=g+s[0]+"|"+s[1]
        print(g)
    else:
        print("Impossible")
