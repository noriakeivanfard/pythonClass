names =  {"nooria", "reyhane", "mahla"}
names.add("mamad") 
print(names)

names = ["nooria", "reyhane", "mahla","mamad"]
names.remove("mamad")
print(names)

names = ["nooria", "reyhane", "mahla","mamad"]
x = names.copy()
print(x)

names = ["nooria", "reyhane", "mahla","mamad"]
names.clear()
print(names)

names = {"nooria", "reyhane", "mahla","mamad"}
names.discard("mamad") 
print(names)


information = {
  "name": "nooria",
  "last_name": "kevanfard",
   "age": 13
}

information.update({"favorite color": "green"})

print(information)
