import os
import argparse

def getArg():
    arg = argparse.ArgumentParser(description='Choose the directory of the Icons.')
    arg.add_argument('-d', '--directory-path', nargs=1, type=str, \
        help='Set a directory path either '\
            'from your working directory or from root directory.')

currentDir = os.getcwd()




if __name__ == '__main__':
    location = input("Please specify a path (Starting from where you are): ")

    files = os.listdir(location)

    for file in files:
        f = open(f"{currentDir}/{location}/{file}", "r")
        lines = f.readlines()
        for i in range(len(lines)):
            if ".ColorScheme-Text { color:#dfdfdf; } .ColorScheme-Highlight { color:#4285f4; } .ColorScheme-NeutralText { color:#ff9800; } .ColorScheme-PositiveText { color:#4caf50; } .ColorScheme-NegativeText { color:#f44336; }" in lines[i]:
                print(file)
                f.close()
                f = open(f"{currentDir}/{location}/{file}", "w")
                lines[i] = "   .ColorScheme-Text { color:#fbf1c7; } .ColorScheme-Highlight { color:#458588; } .ColorScheme-NeutralText { color:#fe8019; } .ColorScheme-PositiveText { color:#689d6a; } .ColorScheme-NegativeText { color:#cc241d; }"
                for line in lines:
                    f.write(f"{line}\n")
                f.close()
            else:
                f.close()
