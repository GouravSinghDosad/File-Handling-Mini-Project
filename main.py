
# from pathlib import Path

# def structure():
#     path = Path('')
#     # items = list(path.rglob('*'))
#     # for i, items in enumerate(items):
#     #     print(f"{i+1} : {items}")
import os


def createFile():
    try:
        name = input("Enter your file name: ")

        if os.path.exists(name):
            print("File already Exists")
        else:
            file = open(f"{name}", 'x')

            data = input("Enter anything you want to add in file: \n")
            file.write(f"{data}")

            file.close()
    except Exception as err:
        print(f"An error occured: {err}")

def reading():

    name = input("Enter the file that you want to read: ")
    
    if os.path.exists(name):
        file = open(f"{name}", 'r')
        print(file.read(), "\n")
        file.close()
    else:
        print("File doesn't exists")

def updateFile():

    fileName = input("Enter the filename you want to update: \n")
    
    if os.path.exists(fileName):
        file = open(f"{fileName}", 'a')

        text = input("Enter the text: \n")
        file.write(f"{text}" + "\n")

        file.close()
    else:
        print("File doesn't exists. Hence, creating a new file")
        file = open(f"{fileName}", 'a')

        text = input("Enter the text: \n")
        file.write(f"{text}" + "\n")

        file.close()

def overwriteFile():

    fileName = input("Enter the filename you want to overwrite: \n")
    
    if os.path.exists(fileName):
        file = open(f"{fileName}", 'w')

        text = input("Enter the text: \n")
        file.write(f"{text}" + "\n")

        file.close()
    else:
        print("File doesn't exists. Hence, creating a new file")
        file = open(f"{fileName}", 'w')

        text = input("Enter the text: \n")
        file.write(f"{text}" + "\n")

        file.close()

def deleteFile(fileName):


    if not os.path.exists(fileName):
        print(f"{fileName}, No such file exists")
    else:
        os.remove(fileName)


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for update a file")
print("Press 4 for delete a file")

option = int(input("Enter your choice: "))

if option == 1:
    createFile()
elif option == 2:
    reading()
elif option == 3:
    
    val = int(input("If you want to update the file then enter 1 and if overwrite then enter 2: "))

    if val == 1:
        updateFile()
    elif val == 2:
        overwriteFile()
    else:
        print("Entered the wrong 'UPDATE' command")
elif option == 4:

    fileName = input("Enter the name of the file to be deleted: \n")
    deleteFile(fileName)
else:
    print("Unfortunately wrong choice")
