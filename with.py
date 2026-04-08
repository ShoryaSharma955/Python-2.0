
f=open("file.txt")

print(f.read())
f.close()

# the same can be written with a with statement

with open("file.txt") as f:
    print(f.read())

# when you use with, you dont have need to close the statement
