#Aaron James
#Macrosmith pulling algo
import sys
import os
import glob
from pathlib import Path
import time
import pickle

DFiles = []
FFiles = []

def main():
    findDir()
    saveDToFile()
    saveFToFile()
    printFiles()

#Physical Print
def printFiles():
    print("Printing Completed List: . .", end = " ")
    time.sleep(2)
    print(".")
    for value in DFiles:
        print(value)
    for value in FFiles:
        print(value)
    print("Printing completed")

#Saves dir to list
def saveDToFile():
    lengthOfD = len(DFiles)
    fileName = input("Please input your directory file name: ")
    fullFileName = fileName + ".txt"
    outF = open(str(fullFileName), 'w')
    outF.write("[")
    for line in DFiles:
        lengthOfD = lengthOfD - 1
        if lengthOfD >= 1:
            outF.write(line + ",") #formatting
        else:
            outF.write(line)
    outF.write("]")
    outF.close()

#saves files to list         
def saveFToFile():
    lengthOfF = len(FFiles)
    fileName = input("Please input your file's file name: ")
    fullFileName = fileName + ".txt"
    outF = open(str(fullFileName), 'w')
    outF.write("[")
    for line in DFiles:
        lengthOfF = lengthOfF - 1
        if lengthOfF >= 1:
            outF.write(line + ",") #formatting
        else:
            outF.write(line)
    outF.write("]")
    outF.close()
    
def findDir():
    print("pulling data: . .", end=" ")
    time.sleep(2)
    print(".")
        
    for root, dirs, files in os.walk('/'):
        for direct in dirs:
            DFiles.append(os.path.join(root, direct)) #formatting
        for file in files:
            FFiles.append(os.path.join(root, file))
    print("")
    print("Data dump completed")
    print("Processing data: . .", end = " ")
    time.sleep(2)
    print(".")

main()
