import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

a=int(input("How many folder do you want to create: "))
for i in range(a):
    name=input("folder name:" )
    createFolder('./'+name+'/')
