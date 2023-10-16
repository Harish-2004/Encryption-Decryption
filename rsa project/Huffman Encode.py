import pickle
db=open("dictionary","rb")
huff=pickle.load(db)
db.close()
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)
def funct(a):
    st=""
    x=len(a)%7
    b=0
    for i in range(0,len(a)-x,7):
        temp_data=int(a[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        st=st+chr(decimal_data)
    if(x!=0):
        b=a[-x:]+"0"*(7-x)
        st+=chr(BinaryToDecimal(int(b)))
    print("x=",x)
    return st
f=open("text.txt")
s=f.read()
f.close()
s1=""
for i in s:
    s1+=huff[i]
print(s1)
encoded=funct(s1)
f=open("huffed","w", encoding="utf-8")
f.write(encoded)
f.close()
