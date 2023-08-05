import pyttsx3
import gtts
S = pyttsx3.init()
S.say("please type your str1")
S.runAndWait()
str_1 = input("enter your str1: ")
S.say("please type your str2")
S.runAndWait()
str_2 = input("enter your str2: ")
S.say("please type your str3")
S.runAndWait()
str_3 = input("enter your str3: ")
if len(str_1) > len(str_2) > len(str_3):
    Result = str_1
    S.say(f" The longest string{str_1}")
    S.runAndWait()
    x = gtts.gTTS(str_1,lang="en",slow = False)
    x.save("sound.mp3")
elif len(str_2) > len(str_1) > len(str_3):
    Result = str_2
    S.say(f" The longest string{str_2}")
    S.runAndWait()
    x = gtts.gTTS(str_2,lang="en",slow = False)
    x.save("sound.mp3")
elif len(str_3) > len(str_1) > len(str_2):
    Result = str_3
    S.say(f" The longest string{str_3}")
    S.runAndWait()  
    x = gtts.gTTS(str_3,lang="en",slow = False)
    x.save("sound.mp3") 
