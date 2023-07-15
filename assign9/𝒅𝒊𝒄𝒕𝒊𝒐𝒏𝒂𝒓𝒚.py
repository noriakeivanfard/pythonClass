names = ['nooria', 'mahla', 'reyhane', 'mamad']
x = names.copy()
print(x)

####################################################

names =  {"nooria", "kiana", "mahla"}

names.clear()
print(names)

####################################################

names = ["nooria", "kiana", "mahla"]

x = names.pop(1)
print(x)
print(names)

####################################################

informatien = {
  "name": "nooria",
  "last name": "kevanfard",
   "age": 13
}

informatien.update({"favorit color": "green"})

print(informatien)

######################################################

informatien = {
  "name": "nooria",
  "last name": "kevanfard",
   "age": 13
}

x = informatien.keys({"favorit color": "green"})

print(x)

########################################################

informatien = {
  "name": "nooria",
  "last name": "kevanfard",
   "age": 13
}

x = informatien.values()

print(x)

#########################################################

informatien = {
  "name": "nooria",
  "last name": "kevanfard",
   "age": 13
}

x = informatien.items()

print(x)

###########################################################

informatien = {
  "name": "nooria",
  "last name": "kevanfard",
   "age": 13
}

x = informatien.get('age')

print(x)
