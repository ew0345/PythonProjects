import tkinter as tk
import os
import subprocess
from random import choice as rc

def returnToLauncher():
    try:
        subprocess.Popen(["py", "launcher.py"])
        root.quit()
    except Exception as e:
        print(f"Failed to launch launcher.py: {e}")

def generateString(length, amount, type):
    # Create File for Storing Strings
    fileStr = os.path.expanduser("~")+"/GeneratedStrings.txt"

    # Convert type to a numberical value
    typeDict = {opt[i]: i for i in range(len(opt))}
    type = typeDict[type]

    # List of Characters to be selected from when generating a string
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbolsBase = ["`", "-", "=", "[", "]", "\\", ";", "\'", ",", ".", "/"]
    symbolsModifiers = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?"]
    lettersUppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lettersLowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    # Combinations to be selected from by 'type' variables when generating and saving strings
    typeOpts = {
        0: [numbers, symbolsBase, symbolsModifiers, lettersUppercase, lettersLowercase],
        1: [lettersUppercase, lettersLowercase],
        2: [numbers, lettersUppercase, lettersLowercase],
        3: [lettersUppercase, lettersLowercase, symbolsBase, symbolsModifiers],
        4: [lettersUppercase, lettersLowercase, symbolsModifiers],
        5: [lettersUppercase, lettersLowercase, symbolsBase],
        6: lettersUppercase,
        7: [numbers, lettersUppercase],
        8: [lettersUppercase, symbolsBase, symbolsModifiers],
        9: [lettersUppercase, symbolsModifiers],
        10: [lettersUppercase, symbolsBase],
        11: lettersLowercase,
        12: [numbers, lettersLowercase],
        13: [lettersLowercase, symbolsBase, symbolsModifiers],
        14: [lettersLowercase, symbolsModifiers],
        15: [lettersLowercase, symbolsBase],
        16: numbers,
        17: [numbers, symbolsBase, symbolsModifiers],
        18: [numbers, symbolsModifiers],
        19: [numbers, symbolsBase],
        20: [symbolsModifiers, symbolsBase],
        21: symbolsModifiers,
        22: symbolsBase

    }

    # Save strings
    with open(fileStr, "w") as f:
        for i in range(amount):
            fullStr = ""
            print(f"{i+1}: ", end="")
            for i1 in range(length):
                str = ""

                opts = typeOpts[type]
                str += rc(rc(opts))

                print(str, end="")
                fullStr += str
            
            f.write(f"{fullStr}\n\n")
            print("")
            fullStr = ""


def init():
    # Create GUI
    global root
    root = tk.Tk()
    root.geometry("300x200")
    root.title("StrGen")
    try:
        root.iconbitmap("images/Icon3.ico")
    except Exception:
        root.iconbitmap()
    
    # Menubar
    menu = tk.Menu(root)
    menuFile = tk.Menu(menu, tearoff=0)
    menuFile.add_command(label="Return to Launcher", command=returnToLauncher)
    menu.add_cascade(label="File", menu=menuFile)
    root.config(menu=menu)

    # Labels
    labelStrLength = tk.Label(root, text="String Length")
    labelStrLength.place(x=20, y=5)

    labelStrAmount = tk.Label(root, text="String Amount")
    labelStrAmount.place(x=110, y=5)

    labelStrType = tk.Label(root, text="Type of String")
    labelStrType.place(x=20, y=60)

    # Spinbox
    sbStrLength = tk.Spinbox(root, width=10)
    sbStrLength.insert(0, "10")
    sbStrLength.place(x=20, y=30)

    sbStrAmount = tk.Spinbox(root, width=10)
    sbStrAmount.insert(0, "10")
    sbStrAmount.place(x=110, y=30)

    # Dropdowns
    global opt;
    opt = ["All", "Letters", "Letters & Numbers", "Letters & Symbols", "Letters & Modifier Symbols", "Letters & Base Symbols", "Uppercase Letters", "Uppercase Letters & Numbers", "Uppercase Letters & Symbols", "Uppercase Letters & Modifier Symbols", "Uppercase Letters & Base Symbols", "Lowercase Letters", "Lowercase Letters & Numbers", "Lowercase Letters & Symbols", "Lowercase Letters & Modifier Symbols", "Lowercase Letters & Base Symbols", "Numbers", "Numbers & Symbols", "Numbers & Modifier Symbols", "Numbers & Base Symbols", "Symbols", "Modifier Symbols", "Base Symbols"]
    ddOpt = tk.StringVar(root)
    ddOpt.set(opt[0])
    ddStrType = tk.OptionMenu(root, ddOpt, *opt)
    ddStrType.place(x=10, y=90)

    # Buttons
    buttonGenerate = tk.Button(root, text="Generate", width=40, command=lambda: generateString(int(sbStrLength.get()), int(sbStrAmount.get()), ddOpt.get()))
    buttonGenerate.place(x=4, y=147)


    root.mainloop()
init()