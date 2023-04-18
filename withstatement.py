k=['t\n','y\n','u','y']
with open('demo1.txt','r+') as f1:
    f1.writelines(k)
    f1.seek(0)
    pp=f1.read()
    print(pp)