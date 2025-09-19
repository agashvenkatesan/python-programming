class stud :
     def __init__(self,a,b,c,m1,m2,m3):
            self.sno=a
            self.sname=b
            self.sage=c
            self.mark1=m1
            self.mark2=m2
            self.mark3=m3
            
     def calculate(self) :
           self.total=self.mark1+self.mark2+self.mark3
           self.avrg=self.total/3
           
           if self.mark1>40 and self.mark2>40 and  self.mark3>40 :
                    self.result='Pass'
           else :
                    self.result='Fail'
          
     
     
     def  disp(self):
           print('std No:',self.sno)
           print('std Nmae:',self.sname)
           print('std Age:',self.sage)
           print('mark1:',self.mark1)
           print('mark2',self.mark2)
           print('mark3',self.mark3)
           print('total:',self.total)
           print('Result',self.result)
           print('average:',self.avrg)
       
x=int(input('Enter no :'))
y=input('Enter Name :')
z=int(input('Enter Age:'))
m1=int(input('Enter m1:'))
m2=int(input('Enter m2:'))
m3=int(input('Enter m3:'))
ob=stud(x,y,z,m1,m2,m3)
ob.calculate()
ob.disp()
           
