# Grading Helper v0
# Written by David Treder

import os, fnmatch, shutil


#Set equal to the folder containing all submissions
#Example: C:\\Users\\NAME\\Downloads\\HW2Submissions
SUBMISSIONS = "C:\\Users\\dedem\\Desktop\\Stevens\\Junior\\CS115\\submissiosn\\hw4submissions"


#Set equal to the folder with the test script
#This can be the same folder as SUBMISSIONS or a different one
TESTING = "C:\\Users\\dedem\\Desktop\\Stevens\\Junior\\CS115\\submissiosn\\testing"


#Set equal to the name of the file in the test script (eg. Lab2.py)
TESTING_NAME = "hw4.py"


#Set equal to the name of your editor of choice
#This is used to open the file after it is found. Leave blank to not open file.
EDITOR_NAME = "idle"


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def selectFromList(lst):
    for x in range(len(lst)):
        print(str(x+1)+". "+lst[x])
    s = int(input("Input a selection as a number: "))
    if len(lst) >= s >= 1:
        return lst[s-1]
    else:
        return ""

def copyFile(p):
    #Deleting old file
    if os.path.exists(TESTING + "\\" + TESTING_NAME):
        os.remove(TESTING + "\\" + TESTING_NAME)

    #Copying
    shutil.copy(p, TESTING + "\\"+TESTING_NAME)
    print("DONE!")

def openFile():
    if (EDITOR_NAME != ""):
        os.system(EDITOR_NAME + " " + TESTING + "\\"+TESTING_NAME)


print("Welcome to Grading Helper. Follow the instructions on screen to select a file.")
print("When the file is opened, the program will freeze until you close the window.")
print("To exit, type EXIT as the student name")
while(True):
    name = input("Input first few letters of last name of student: ")
    if (name == "EXIT"):
        break
    results = find(name + "*", SUBMISSIONS)
    if not results:
        print("No students found.")
    elif len(results) > 1:
        print("Multiple students found")
        s = selectFromList(results)
        if s != "":
            copyFile(s)
            openFile()
    elif len(results) == 1:
        print("Found submission.")
        print(results[0])
        copyFile(results[0])
        openFile()
        
    else:
        print("Something broke!")
