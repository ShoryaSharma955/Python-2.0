class employee:
    company="ITC"
    name="shorya"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company} ")

class coder:
    language="python"
    def printLanguages(self):
        print(f"Out of all these language here is your language {self.language}")

class programmer(employee,coder):
    company="HCL"
    def showLanguage(self):
        print(f"The name of the company is {self.company} and the salary is {self.language} ")
    
a=employee()
b=programmer()
# print(a.company,b.company)
b.showLanguage()
b.show()    
b.printLanguages()

