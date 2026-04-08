# Write a python program to rename a file to “renamed_by_ python.txt.

with open("self.txt") as f:
    content=f.read()

with open("renamed_by_pthon.txt" ,"w") as f:
    f.write(content)