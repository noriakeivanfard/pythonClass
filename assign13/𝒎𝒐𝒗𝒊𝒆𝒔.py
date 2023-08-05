txt = open(r"D:/NOORIA/computer/assign13/movies.txt")
dataa = txt.readlines()
dictt = {}

op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_Movies in alphabetical order
5_exit
which one?""")) 

def read_data():
  for i in dataa:
      data_ = i.rstrip()
      name, IMDB = data_.split("  ")
      dictt[name] = IMDB
  return dictt  

def show_add(dictt):
  N = input("enter name of movie: ")
  I = float(input("entre movie IMDB: "))
  dictt.update({N:str(I)})
  return dictt 

def show_movies():
  for i in sorted(dictt.keys()):
        print(i, dictt[i])

def show_IMDB(dictt):
  dict = sorted(dictt.values(), reverse=True)  
  for i in range(5):
    for j in dictt.keys():
      if dict[j] == dict[i]:
        print(dict[i], j) 
        
def exit_(dict):
    file = open()
    for i in dict.keys():
        str = i + " " + dict[i]+ "\n"
        file.write(str)
 
if op == 1:
  show_add(dictt)
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    exit(0) 
  elif ask == "y":
    op=int(input("""
 1_add movie
 2_Display the file
 3_five movies with the highest scores
 4_Movies in alphabetical order
 5_exit
 which one?"""))
 
elif op == 2:
  show_movies(dictt)
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    exit(0) 
  elif ask == "y":
    op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_Movies in alphabetical order
5_exit
which one?""")) 

elif op == 3:         
  show_IMDB(dictt) 
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    exit(0) 
  elif ask == "y":
    op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_Movies in alphabetical order
5_exit
which one?""")) 
  
elif op == 4:
     exit_(dictt) 
