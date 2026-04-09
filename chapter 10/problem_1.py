'''Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''

class programmer:
    company="Microsoft"
    
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

p=programmer("Shorya",90000000,121004)
print(p.name,p.salary,p.pincode,p.company)
r=programmer("rohan",70000000,121666)
print(r.name,r.salary,r.pincode,r.company)
    