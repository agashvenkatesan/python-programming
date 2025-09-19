n=int(input('Enter the no.of terms:'))
sum=0
i=0
for i in range (1,n+1):
    sum+=1/i**2
    i+=1
print('The sum of the series is',sum)
