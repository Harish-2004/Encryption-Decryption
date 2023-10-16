def en(l,e,n):
    step1=[]
    for i in l:
        step1.append((i**e)%n)
    print(step1)
    return step1
def mixer1(l):
    new_str=""
    for i in l:
        new_str+=chr(i)
    return new_str
f=open("huffed","r")
string=f.read()
f.close()
s=[]
for i in string:
    s.append(ord(i))
print(s)
while True:
    lock=input("enter the public key").split()
    if len(lock)==2:
        break
    else:
        print("invalid")
lock[0]=int(lock[0])
lock[1]=int(lock[1])
cipher=en(s,lock[0],lock[1])
print("total encrypted=",mixer1(cipher))
f=open("encrypted2","w",encoding="utf-8")
f.write(mixer1(cipher))
f.close()