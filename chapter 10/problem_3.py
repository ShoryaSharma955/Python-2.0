'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?
'''

class demo:
    a=5

object=demo()
print(object.a) #prints the class attribute bcz instanve attribute is not present
object.a=0   #instance attribute is set

print(object.a)  #prints instance attribute bcz instance attribute is present
print(demo.a)  #prints the class attribute