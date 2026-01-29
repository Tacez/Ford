import random

def getUnusedThemes(filename):
    # Find all files
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    #Randomize one theme
    pickedTheme = random.choice(lines)
    
    return pickedTheme

def moveToUsedThemes(unusedFile, usedFile, theme):
    # Find and remove theme from used file
    with open(unusedFile, "r") as f:
        lines = f.readlines()
        lines.remove(theme)
    with open(unusedFile, "w") as f:
        f.writelines(lines)

    # Add theme to usedThemes
    with open(usedFile, "a") as f:
        f.write(theme)
        
if __name__ == "__main__":
    themeFound = False

    while not themeFound:
        theme = getUnusedThemes("themeList.txt")
        boolOk = input(theme + "\nIs this theme okay?")

        if (boolOk == "y" or boolOk == "yes"):
            print("Perfect! Moving theme to list of used themes")
            themeFound = True
        else:
            print("Okay, redrawing new theme")

    moveToUsedThemes("themeList.txt", "usedThemes.txt", theme)

