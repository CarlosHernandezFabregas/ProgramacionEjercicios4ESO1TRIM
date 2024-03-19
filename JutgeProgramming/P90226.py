a=input()
lista1=a.split()
c=lista1[0]
d=lista1[1]
if c<d:
    print(c,"<",d)
if d<c:
    print(c,">",d)
if c==d:
    print(c,"=",d)