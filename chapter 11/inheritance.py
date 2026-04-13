class employee:
    company="ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} ")


class programmer(employee):
    company="HCL"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} ")

a=employee()
b=programmer()
print(a.company,b.company)
