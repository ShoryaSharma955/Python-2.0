class employee:
    salary=1000000
    language="python"

    def getInfo(self):
        print(f"The language is {self.language}.  The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")


shorya=employee()
shorya.language="java"
shorya.greet()
shorya.getInfo()