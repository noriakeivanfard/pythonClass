txt = open(r"D:/NOORIA/computer/assign13/movies.txt" ,"r")
dataa = txt.readlines()
dictt = {}

for film in dataa:
  data_ = film.rstrip()
  name, IMDB = data_.split("  ")
  dictt[name] = IMDB
print(dictt)

op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_exit
which one?""")) 


def show_add(dictt):
  N = input("enter name of movie: ")
  I = float(input("entre movie IMDB: "))
  dictt.update({N:str(I)})
  return dictt

def show_movies(dictt):
    for i in sorted(dictt.keys()):
                print(i, dictt[i])

def show_imdb(dict):
    diict = sorted(dict.values(), reverse=True)  
    for i in range(5):
        for j in dict.keys():
            if dict[j] == diict[i]:
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
 4_exit
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
4_exit
which one?""")) 

elif op == 3:         
  show_imdb(dictt) 
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    exit(0) 
  elif ask == "y":
    op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_exit
which one?""")) 
  
elif op == 4:
     exit_(dictt) 
