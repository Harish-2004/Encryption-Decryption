import pickle
db=open("dictionary","rb")
huff=pickle.load(db)
db.close()
def retrieve(st,x):
    a=""
    if(x==0):
        b=st[:]
    else:
        b=st[:-1]
    for i in b:
        ascii_val = ord(i)
        binary_val = bin(ascii_val)
        binary_val = str(binary_val[2:])
        #print(binary_val)
        if len(binary_val)<7:
            binary_val="0"*(7-len(binary_val))+binary_val
        a = a + binary_val
        #print(binary_val)
        #a = a + str(binary_val[2:])
    if x!=0:
        ascii_val = ord(st[-1])
        binary_val = bin(ascii_val)
        binary_val=str(binary_val[2:2+x])
        a = a + binary_val

    return a
def function(x):
    for i in huff.keys():
        if (huff[i] == x):
            return i
        else:
            continue
f=open("huffed","r")
st=f.read()
f.close()
retrieve(st,0)
t=""
new=""
x=int(input("enter left out bits"))
a=retrieve(st,x)
#print(a)
for i in a:
    t+=i
    if t in huff.values():
        new+=function(t)
        t=""
print(new)
