import pyttsx3
engine = pyttsx3.init()
engine.say("please type your str1")
engine.runAndWait()
str_1 = input("enter your str1: ")
engine.say("please type your str2")
engine.runAndWait()
str_2 = input("enter your str2: ")
engine.say("please type your str3")
engine.runAndWait()
str_3 = input("enter your str_3: ")
if len(str_1) > len(str_2) > len(str_3):
    Result = str_1
    engine.say(f" The longest string{str_1}")
    engine.runAndWait()
elif len(str_2) > len(str_1) > len(str_3):
    Result = str_2
    engine.say(f" The longest string{str_2}")
    engine.runAndWait()
elif len(str_3) > len(str_1) > len(str_2):
    Result = str_3
    engine.say(f" The longest string{str_3}")
    engine.runAndWait() 
