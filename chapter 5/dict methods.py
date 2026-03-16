marks={
    "shorya":100,
    "sonu":20,
    "pardeep":29,
    0:"sahil"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shorya":90})
print(marks)

print(marks.get("shorya")) 
print(marks["shorya"])   

print(marks.get("shorya2")) #returns none
print(marks["shorya2"])     #returns error