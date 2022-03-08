import os
from os import close
from gtts import gTTS
print("Note that the file must be in txt formate")
flocal=input("full file location with name here \(no need to add extention\): ")
flocal=flocal+".txt"
print(flocal)
f = open(flocal, "r")
mytext = f.read()
language = 'en'
myobj = gTTS(text=mytext,tld='co.in', lang=language, slow=True)
fnam=input("Enter audio file name to save: ")
aflocal=input("Audio file location: ")
myobj.save(aflocal+"\\"+fnam+".m4a")
f.close()
os.system("start "+aflocal+"\\"+fnam+".m4a")