'''If languages of two friends are same; what will happen to the program in problem
6?'''

# Answer= 2 different values can appear but not keys

d={}

name=input("Enter friend name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friend name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friend name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friend name: ")
lang=input("Enter language name: ")
d.update({name: lang})

print(d)
