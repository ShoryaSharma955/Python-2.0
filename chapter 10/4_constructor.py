class employee:
    salary=1000000
    language="python"

    def __init__(self,name,salary,language):  #dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    # def getInfo(self):
    #     print(f"The language is {self.language}.  The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")


shorya=employee("shorya",1000000,"java")
print(shorya.name,shorya.salary,shorya.language)
# shorya.language="java"
shorya.greet()
# shorya.getInfo()