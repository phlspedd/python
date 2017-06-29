#!/usr/bin/python3

import sys
import os

#print(len(sys.argv))

#ProjectFolder | ProjectName | pythonVersion
if len(sys.argv) != 4:
    print("Wrong usage. Please inform project folder, then projectName and python version.")
    sys.exit(1)

projectFolder = sys.argv[1]
projectName = sys.argv[2]
pythonVersion = sys.argv[3]

os.mkdir(projectFolder)
os.chdir(projectFolder)
os.mkdir(projectName)
os.chdir(projectName)
os.system("virtualenv -p $( which pythonVersion ) ./projectName")
