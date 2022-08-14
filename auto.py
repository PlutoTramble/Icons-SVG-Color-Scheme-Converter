import os
import argparse
import sys
import numpy as np

listOfColors_Gruvbox = [['list', 'of', 'colors'], ['list', 'of', "list"]]

# Get command argument
def getArg():
    arg = argparse.ArgumentParser(description='Choose the directory of the Icons.')
    arg.add_argument('-d', '--directory-path', type=str, \
        help='Set a directory path either '\
            'from your working directory or from root directory.', \
        dest='Directory')

    args = arg.parse_args()

    return args

def getClosestColor(listColors, color):
    listColors = np.array(listColors)
    color = np.array(color)
    difference = np.sqrt(np.sum((listColors-color)**2,axis=1))
    indexSmallest = np.where(difference=np.amin(difference))
    smallestDifference = listColors[indexSmallest]

    return smallestDifference

if __name__ == '__main__':
    currentDir = f"{os.getcwd()}/"
    args = getArg()
    location = args.Directory
    files = os.listdir(location)

    if location[0] == '/':
        currentDir = ""

    
    for file in files:
        f = open(f"{currentDir}{location}/{file}", "r")
        lines = f.readlines()
        f.close()

        #Scanning lines
        filled = False
        stroked = False
        timesColored = 0
        for i in range(len(lines)):
            if ("fill:#" in lines[i] or "fill=\"#" in lines[i]):
                print(f"Filling in file '{file}' in line {i}")
                #Do conversion and replace num and write file
            
            if "stroke=\"#" in lines[i]:
                print(f"Filling in file '{file}' in line {i}")
                #Do conversion and replace num and write file

            if (".ColorScheme-Text { color:#dfdfdf; } "\
                ".ColorScheme-Highlight { color:#4285f4; } "\
                ".ColorScheme-NeutralText { color:#ff9800; } "\
                ".ColorScheme-PositiveText { color:#4caf50; } "\
                ".ColorScheme-NegativeText { color:#f44336; }" in lines[i]):

                print(f"Changing color scheme in file {file} in line {i}")
                #Do conversion and replace num and write file
