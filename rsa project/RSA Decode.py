def de(l,d,n):
    op=[]
    for i in l:
        op.append((i**d)%n)
    print(op)
    return op
def seperator(n):
    l=[]
    for i in n:
        l.append(ord(i))
    print(l)
    return l
def converter(l):
    s = ""
    for i in l:
        s += chr(i)
    return s
f=open("encrypted2","r",encoding="utf-8")
encrypted=f.read()
f.close()
to_be_decrypted=seperator(encrypted)
key=list(map(int,input("enter the private key").split()))
ans=de(to_be_decrypted,key[0],key[1])
#print("decrypted=",ans)
s=converter(ans)
print(s)
file=open("decrypted","w")
file.write(s)
file.close()