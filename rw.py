f=open('demo1.txt','r+')
print(f.tell())
print(f.read())
print(f.tell())
print(f.read())
print(f.tell())
print(f.seek(0))
f.write('computer science')
print(f.read())