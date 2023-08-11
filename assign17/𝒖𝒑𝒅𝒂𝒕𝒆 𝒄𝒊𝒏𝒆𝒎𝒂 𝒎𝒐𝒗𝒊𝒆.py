import sqlite3

txt = open(r"D:/NOORIA/computer/assign17/movies.txt" ,"r")
dataa = txt.readlines()
dictt = {}

for film in dataa:
  data_ = film.rstrip()
  name, IMDB = data_.split("  ")
  dictt[name] = IMDB
print(dictt)

conne = sqlite3.connect("movies.db")
c = conne.cursor()

op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_exit
which one?""")) 


c.execute("""
    CREATE TABLE media (
             name TEXT,
             imdb TEXT
    ) 
 """)

def show_add():
  name = input("enter name of movie: ")
  imdb = float(input("entre movie IMDB: "))
  c.execute("INSERT INTO media VALUES (?, ?)",name,imdb)
  conne.commit()
  
def show_movies():
    c.execute("SELECT * FROM customers")

itames = c.fetchall()

for itam in itames:
    print(itam)
    
def show_imdb():
    c.execute("SELECT * FROM media ORDER BY imdb DESC") 
item = c.fetchall() 
for i in range(5):
    try:
        print(item[i])
    except:
        pass 

if op == 1:
  show_add()
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    conne.close()
  elif ask == "y":
    op=int(input("""
 1_add movie
 2_Display the file
 3_five movies with the highest scores
 4_exit
 which one?"""))
 
elif op == 2:
  show_movies()
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
   conne.close() 
  elif ask == "y":
    op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
_exit
which one?""")) 

elif op == 3:         
  show_imdb() 
  ask = input("do you want to try again?(y, n):")
  if ask == "n":
    conne.close() 
  elif ask == "y":
    op=int(input("""
1_add movie
2_Display the file
3_five movies with the highest scores
4_exit
which one?""")) 
  
elif op == 4:
     conne.close()
     
conne.commit()
conne.close() 
