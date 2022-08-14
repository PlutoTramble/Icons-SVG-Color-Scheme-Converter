import os
import argparse
import sys
import numpy as np

listOfColors_Gruvbox_dark = [\
    [29, 32, 33], \
    [40, 40, 40], \
    [50, 48, 47], \
    [60, 56, 54], \
    [80, 73, 69], \
    [102, 92, 84], \
    [124, 111, 100], \
    [146, 131, 116], \
    [168, 153, 132], \
    [189, 174, 147], \
    [213, 196, 161], \
    [235, 219, 178], \
    [251, 241, 199], \
    [214, 93, 14], \
    [254, 128, 25], \
    [204, 36, 29], \
    [251, 73, 52], \
    [152, 151, 26], \
    [184, 187, 38], \
    [215, 153, 33], \
    [250, 189, 47], \
    [69, 133, 136], \
    [131, 165, 152], \
    [177, 98, 134], \
    [211, 134, 155], \
    [104, 157, 106], \
    [142, 192, 124] \
]

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
    indexSmallest = np.where(difference==np.amin(difference))
    smallestDifference = np.array(listColors[indexSmallest]).tolist()

    return smallestDifference

def getConvertedColor(line:str, whatToFind:str):
    lineIndex = line.find(whatToFind) + len(whatToFind)
    colorHex = ""

    #read color from line
    for i in range(6):
        colorHex += line[lineIndex]
        lineIndex += 1
    
    lineIndex -= 7 # Reset lineIndex

    colorRGB = list(int(colorHex[i:i+2], 16) for i in (0, 2, 4))
    newColorRGB = getClosestColor(listOfColors_Gruvbox_dark, colorRGB)[0]
    newColorHex = ('{:X}{:X}{:X}').format(\
        newColorRGB[0], newColorRGB[1], newColorRGB[2]).lower()

    # Write brand new line
    newLine = ""
    index_treshold_before_color = lineIndex
    index_treshold_after_color = index_treshold_before_color + 6
    color_string_index = 0
    for i in range(len(line) - 1): 
        if i > index_treshold_before_color and i <= index_treshold_after_color:
            newLine += newColorHex[color_string_index]
            print(color_string_index)
            color_string_index += 1
        else:
            newLine += line[i]

    return newLine


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
                new_line = getConvertedColor(lines[i], "fill:#")
                lines[i] = new_line

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

        #f = open(fullPath, "w")

        for line in lines:
            print(line)
