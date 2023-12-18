import tkinter as tk
import subprocess

def returnToLauncher():
    try:
        subprocess.Popen(["py", "launcher.py"])
        root.quit()
    except Exception as e:
        print(f"Failed to launch launcher.py: {e}")

def calculate(userLevel, spotLevel):
    # Convert userLevel & spotLevel str to int
    userLevel = int(userLevel); spotLevel = int(spotLevel)
    
    # Set values to max/min if they are too low or too high
    if (userLevel > 120): userLevel = 120
    if (spotLevel > 120): spotLevel = 120
    if (userLevel < 1): userLevel = 1
    if (spotLevel < 1): spotLevel = 1

    # Tome math
    tomeChance = round((userLevel + spotLevel) / 250000, 6)
    labelChance.config(text=f"{tomeChance}")
    

def init():
    global root
    root = tk.Tk()
    # Set Window Size
    root.geometry("253x215")
    # Set Window Title
    root.title("Tome Calc")
    # Set Application Icon
    try:
        root.iconbitmap("./images/Icon3.ico")
    except Exception:
        root.iconbitmap()

    # Images
    try:
        image = tk.PhotoImage(file="./images/Icon3.png")
    except tk.TclError:
        image = tk.PhotoImage()

    # Menubar
    menu = tk.Menu(root)

    menuFile = tk.Menu(menu, tearoff=0)
    menuFile.add_command(label="Return to Launcher", command=returnToLauncher)

    menu.add_cascade(label="File", menu=menuFile)
    root.config(menu=menu)

    # Labels
    labelUserLevel = tk.Label(root, text="User Level")
    labelUserLevel.place(x=4, y=35)

    labelSpotLevel = tk.Label(root, text="Spot Level")
    labelSpotLevel.place(x=4, y=60)

    global labelChance
    labelChance = tk.Label(root)
    labelChance.place(x=34, y=120)

    labelImage = tk.Label(root, image=image)
    labelImage.place(x=150, y=35)

    labelMadeBy = tk.Label(root, text="Made By Ew0345")
    labelMadeBy.place(x=150, y=89)

    # Inputs
    userLevel = tk.Spinbox(root, from_=1, to=120, width=3)
    userLevel.place(x=80, y=35)

    spotLevel = tk.Spinbox(root, from_=1, to=120, width=3)
    spotLevel.place(x=80, y=60)

    # Set Defaults for Spinboxes
    userLevel.delete(0, "end")
    userLevel.insert(0, "120")

    spotLevel.delete(0, "end")
    spotLevel.insert(0, "120")

    # Buttons
    buttonCalculate = tk.Button(root, text="Calculate", command=lambda: calculate(userLevel.get(), spotLevel.get()))
    buttonCalculate.place(x=34, y=85)

    root.mainloop()

init()