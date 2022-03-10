# Grading Helper v0.1
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

#Set to true if you want the next submission to be loaded to be
#the next submission alphabetically. Useful for grading a section
#of students in a row.
SEQUENTIAL = True

#Set to True if you are using Logisim.
LOGISIM_MODE = False

#Set to the name of your logisim jar, placed in the testing folder.
LOGISIM_JAR = "logisim.jar"



def find(pattern, path, includeroot=True):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                if (includeroot):
                    result.append(os.path.join(root, name))
                else:
                    result.append(name)
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
    if (LOGISIM_MODE):
        os.chdir(TESTING)
        os.system("java -jar " + LOGISIM_JAR +" "+ TESTING_NAME)
    elif (EDITOR_NAME != ""):
        os.system(EDITOR_NAME + " " + TESTING + "\\"+TESTING_NAME)

def main():
    print("Welcome to Grading Helper. Follow the instructions on screen to select a file.")
    print("When the file is opened, the program will freeze until you close the window.")
    print("To exit, type EXIT as the student name")
    if (SEQUENTIAL):
        name = input("Input first few letters of last name of student: ")
        results = find(name + "*", SUBMISSIONS, False)
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
            dirlist=os.listdir(SUBMISSIONS)
            index = dirlist.index(results[0])
            while(True):
                print(dirlist[index])
                copyFile(os.path.join(SUBMISSIONS, dirlist[index]))
                openFile()
                index += 1
            
        else:
            print("Something broke!")

    else:
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

if __name__ == "__main__":
    main()



