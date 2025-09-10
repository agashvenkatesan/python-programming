a=[]
n=int(input("Enter a number"))
for i in range (0,n):
    h=int(input("Enter elements "))
    a.append(h)
print("The list is",a)
print(a[-1])
print(a[0])
print(a[-3:])
print(a[3:6])
a.extend([16,21,7])
print(a)
a.insert(2,9)
print(a)




                                                  
