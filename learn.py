import tkinter as tk

def calculate(userLevel, enemyLevel, isIceType, gameGen):
    # Converts userLevel and enemeyLevel to ints
    userLevel = int(userLevel); enemyLevel = int(enemyLevel)

    # Math for accuracy
    if (userLevel >= enemyLevel):
        acc = (userLevel - enemyLevel) + 30
        
        # If game gen is 7 or high then there is -10% hit chance if the user isn't ice type
        if (gameGen == 1 and isIceType == 0): acc -= 10
    else:
        acc = 0
    
    if (acc > 100): acc = 100

    labelChance.config(text=f"Chance to hit: {acc}%")

def init():
    root = tk.Tk()
    # Set Window Size
    root.geometry("250x215")
    # Set Window Title
    root.title("SCC")
    # Set Application Icon
    root.iconbitmap("./Icon3.ico")

    # Images
    image = tk.PhotoImage(file="./Icon3.png")

    # Labels
    labelUserLevel = tk.Label(root, text="User Level")
    labelUserLevel.place(x=4, y=35)
    
    labelEnemyLevel = tk.Label(root, text="Enemy Level");
    labelEnemyLevel.place(x=4, y=60)

    global labelChance
    labelChance = tk.Label(root)
    labelChance.place(x=34, y=120)

    labelImage = tk.Label(root, image=image)
    labelImage.place(x=150, y=35)

    labelMadeBy = tk.Label(root, text="Made By Ew0345")
    labelMadeBy.place(x=150, y=89)

    # Inputs
    userLevel = tk.Spinbox(root, from_=1, to=100, width=3)
    userLevel.place(x=94, y=32)

    enemyLevel = tk.Spinbox(root, from_=1, to=100, width=3)
    enemyLevel.place(x=94, y=57)

    # Set the default values of the Spinboxes
    userLevel.delete(0, "end")
    userLevel.insert(0, "100")

    enemyLevel.delete(0, "end")
    enemyLevel.insert(0, "100")

    # Checkboxes
    gameGenVar = tk.IntVar()
    gameGen = tk.Checkbutton(root, text="Gen 7+", variable=gameGenVar)
    gameGen.place(x=10, y=140)

    isIceTypeVar = tk.IntVar()
    isIceType = tk.Checkbutton(root, text="User is Ice Type?", variable=isIceTypeVar)
    isIceType.place(x=85, y=140)

    # Buttons
    #lambda: calculate(userLevel, enemyLevel, isIceType, gameGen)
    buttonCalculate = tk.Button(root, text="Calculate", command=lambda: calculate(userLevel.get(), enemyLevel.get(), isIceTypeVar.get(), gameGenVar.get()))
    buttonCalculate.place(x=34, y=85)    

    root.mainloop()

init()