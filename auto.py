import os
import argparse
import sys
import numpy as np

listOfColors_Gruvbox_dark = {\
    'bg0_h':[29, 32, 33], \
    'bg or bg0':[40, 40, 40], \
    'bg0_s':[50, 48, 47], \
    'bg1':[60, 56, 54], \
    'bg2':[80, 73, 69], \
    'bg3':[102, 92, 84], \
    'bg4':[124, 111, 100], \
    'gray 245':[146, 131, 116], \
    'fg4 or gray 246':[168, 153, 132], \
    'fg3':[189, 174, 147], \
    'fg2':[213, 196, 161], \
    'fg1 or fg':[235, 219, 178], \
    'fg0':[251, 241, 199], \
    'orange 166':[214, 93, 14], \
    'orange 208':[254, 128, 25], \
    'red 124':[204, 36, 29], \
    'red 167':[251, 73, 52], \
    'green 106':[152, 151, 26], \
    'green 142':[184, 187, 38], \
    'yellow 172':[215, 153, 33], \
    'yellow 214':[250, 189, 47], \
    'blue 66':[69, 133, 153], \
    'blue 109':[131, 165, 152], \
    'purple 132':[177, 98, 134], \
    'purple 175':[211, 134, 155], \
    'aqua 72':[104, 157, 106], \
    'aqua 108':[142, 192, 124] \
    }

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
        fullPath = f"{currentDir}{location}/{file}"
        f = open(fullPath, "r")
        lines = f.readlines()
        f.close()

        #Scanning lines
        filled = False
        stroked = False
        timesColored = 0
        for i in range(len(lines)):
            if "fill:#" in lines[i]:
                print(f"Filling in file '{file}' in line {i}")
                #Do conversion and replace num and write file

            if "fill=\"#" in lines[i]:
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
