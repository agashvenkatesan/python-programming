d={"Empno":1424,"EmpName":"coolie"}
print(d['Empno'])
print(d['EmpName'])
d['Empname']='Akazaa'
print(d)
d['Empage']=17
print(d)
d.pop('EmpName')
print(d)
for key in d:
    print(key)
for value in d.values() :
    print(value)
for key,value in d.items():
    print(key,':',value)
