import os
import tkinter as tk
from tkinter import ttk
import subprocess

def returnToLauncher():
    try:
        subprocess.Popen(["py", "launcher.py"])
        root.quit()
    except Exception as e:
        print(f"Failed to launch launcher.py: {e}")

def writeStates():
    # TODO
    # Majikoi TODO
    # Majikoi S TODO
    # Majikoi A-1
    if mA1BenkiVal.get() == 0:
        mA1States[0] = 0
    else:
        mA1States[0] = 1

    if mA1AzumiVal.get() == 0:
        mA1States[1] = 0
    else:
        mA1States[1] = 1

    if mA1SayakaVal.get() == 0:
        mA1States[2] = 0
    else:
        mA1States[2] = 1

    with open(mA1State, "w") as f:
        for item in mA1States:
            f.write("%s\n" % item)

    # Majikoi A-2
    if mA2MonshiroVal.get() == 0:
        mA2States[0] = 0
    else:
        mA2States[0] = 1
    
    if mA2AiessVal.get() == 0:
        mA2States[1] = 0
    else:
        mA2States[1] = 1
    
    if mA2SeisoVal.get() == 0:
        mA2States[2] = 0
    else:
        mA2States[2] = 1
    
    with open(mA2State, "w") as f:
        for item in mA2States:
            f.write("%s\n" % item)

    # Majikoi A-3 TODO
    # Majikoi A-4 TODO
    # Majikoi A-5 TODO

    root.quit()

def readStates():
    # TODO
    # Majikoi Routes Directory
    dirHome = os.path.expanduser("~")
    dirMaji = "MajikoiRoutesPy"
    global dirPath; dirPath = os.path.join(dirHome, dirMaji)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    # Majikoi States Files
    global mState; mState = dirPath+"/mState.txt"
    global mSState; mSState = dirPath+"/mSState.txt"
    global mA1State; mA1State = dirPath+"/mA1State.txt"
    global mA2State; mA2State = dirPath+"/mA2State.txt"
    global mA3State; mA3State = dirPath+"/mA3State.txt"
    global mA4State; mA4State = dirPath+"/mA4State.txt"
    global mA5State; mA5State = dirPath+"/mA5State.txt"

     # Handle State files

    # Majikoi
    if not os.path.isfile(mState):
        with open(mState, "w") as f:
            f.write("0\n" * 19)
    
    # Majikoi S
    if not os.path.isfile(mSState):
        with open(mSState, "w") as f:
            f.write("0\n" * 37)

    # Majikoi A-1
    global mA1States
    if not os.path.isfile(mA1State):
        with open(mA1State, "w") as f:
            f.write("0\n" * 3)
        with open(mA1State, "r") as f:
            mA1States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mA1State):
        with open(mA1State, "r") as f:
            mA1States = [line.strip() for line in f.readlines()]
    
    # Majikoi A-2
    global mA2States
    if not os.path.isfile(mA2State):
        with open(mA2State, "w") as f:
            f.write("0\n" * 3)
        with open(mA2State, "r") as f:
            mA2States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mA2State):
        with open(mA2State, "r") as f:
            mA2States = [line.strip() for line in f.readlines()]
    
    # Majikoi A-3
    global mA3States
    if not os.path.isfile(mA3State):
        with open(mA3State, "w") as f:
            f.write("0\n" * 3)
        with open(mA3State, "r") as f:
            mA3States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mA3State):
        with open(mA3State, "r") as f:
            mA3States = [line.strip() for line in f.readlines()]
    
    # Majikoi A-4
    global mA4States
    if not os.path.isfile(mA4State):
        with open(mA4State, "w") as f:
            f.write("0\n" * 3)
        with open(mA4State, "r") as f:
            mA4States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mA4State):
        with open(mA4State, "r") as f:
            mA4States = [line.strip() for line in f.readlines()]

    # Majikoi A-5
    global mA5States
    if not os.path.isfile(mA5State):
        with open(mA5State, "w") as f:
            f.write("0\n" * 3)
        with open(mA5State, "r") as f:
            mA5States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mA5State):
        with open(mA5State, "r") as f:
            mA5States = [line.strip() for line in f.readlines()]

def init():
    global root
    root = tk.Tk()
    # Set Window Size
    root.geometry("800x600")
    # Set Window Title
    root.title("Majikoi Routes Tracker")
    # Set Application Icon
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

    # Setup Notebook
    notebook = ttk.Notebook(root)
    tabMaji = ttk.Frame(notebook)
    tabMajiS = ttk.Frame(notebook)
    tabA1 = ttk.Frame(notebook)
    tabA2 = ttk.Frame(notebook)
    tabA3 = ttk.Frame(notebook)
    tabA4 = ttk.Frame(notebook)
    tabA5 = ttk.Frame(notebook)
    tabAbout = ttk.Frame(notebook)

    notebook.add(tabMaji, text="Majikoi")
    notebook.add(tabMajiS, text="Majikoi S")
    notebook.add(tabA1, text="Majikoi A-1")
    notebook.add(tabA2, text="Majikoi A-2")
    notebook.add(tabA3, text="Majikoi A-3")
    notebook.add(tabA4, text="Majikoi A-4")
    notebook.add(tabA5, text="Majikoi A-5")
    notebook.add(tabAbout, text="About")

    notebook.pack(expand=True, fill="both")

    # Majikoi TODO
    # Majikoi S TODO
    # Majikoi A-1
    # Variables
    global mA1BenkiVal; mA1BenkiVal = tk.IntVar()
    global mA1AzumiVal; mA1AzumiVal = tk.IntVar()
    global mA1SayakaVal; mA1SayakaVal = tk.IntVar()

    # Labels
    labelBenki = tk.Label(tabA1, text="Benki", font=("Tahoma", 13))
    labelBenki.place(x=10, y=10)

    labelAzumi = tk.Label(tabA1, text="Azumi", font=("Tahoma", 13))
    labelAzumi.place(x=147, y=10)

    labelSayaka = tk.Label(tabA1, text="Sayaka", font=("Tahoma", 13))
    labelSayaka.place(x=270, y=10)

    # Checkbuttons
    mA1Benki = tk.Checkbutton(tabA1, text="Completed", font=("Tahoma", 11), variable=mA1BenkiVal)
    mA1Benki.place(x=8, y=34)

    mA1Azumi = tk.Checkbutton(tabA1, text="Completed", font=("Tahoma", 11), variable=mA1AzumiVal)
    mA1Azumi.place(x=147, y=34)
 
    mA1Sayaka = tk.Checkbutton(tabA1, text="Completed", font=("Tahoma", 11), variable=mA1SayakaVal)
    mA1Sayaka.place(x=269, y=34)

    # Majikoi A-2 TODO
    # Variables
    global mA2MonshiroVal; mA2MonshiroVal = tk.IntVar()
    global mA2AiessVal; mA2AiessVal = tk.IntVar()
    global mA2SeisoVal; mA2SeisoVal = tk.IntVar()

    # Labels
    labelMonshiro = tk.Label(tabA2, text="Monshiro", font=("Tahoma", 13))
    labelMonshiro.place(x=10, y=10)
    
    labelAiess = tk.Label(tabA2, text="Aiess", font=("Tahoma", 13))
    labelAiess.place(x=147, y=10)
    
    labelSeiso = tk.Label(tabA2, text="Seiso", font=("Tahoma", 13))
    labelSeiso.place(x=270, y=10)

    # Checkbuttons
    mA2Monshiro = tk.Checkbutton(tabA2, text="Completed", font=("Tahoma", 11), variable=mA2MonshiroVal)
    mA2Monshiro.place(x=8, y=34)

    mA2Aiess = tk.Checkbutton(tabA2, text="Completed", font=("Tahoma", 11), variable=mA2AiessVal)
    mA2Aiess.place(x=147, y=34)

    mA2Seiso = tk.Checkbutton(tabA2, text="Completed", font=("Tahoma", 11), variable=mA2SeisoVal)
    mA2Seiso.place(x=269, y=34)

    # Majikoi A-3 TODO
    # Majikoi A-4 TODO
    # Majikoi A-5 TODO
    
    # About
    try: 
        image = tk.PhotoImage(file="images/Icon3.png")
    except tk.TclError:
        image = tk.PhotoImage()

    
    labelImage = tk.Label(tabAbout, image=image)
    labelImage.place(x=249, y=13)

    labelMadeBy = tk.Label(tabAbout, text="Made By Ew0345", font=("Tahoma", 14))
    labelMadeBy.place(x=310, y=30)

    labelGithub = tk.Label(tabAbout, text="Github: https://www.github.com/ew0345", font=("Tahoma", 14))
    labelGithub.place(x=180, y=77)

    labelAboutInfo = tk.Label(tabAbout, text="This program creates a folder and several files in your user home folder\nThe files are all contained within the folder \"MajikoiRoutes\", these can be safely deleted\nHowever deleting these files will reset the state of any checked boxes in the routes tabs.", font=("Tahoma", 14))
    labelAboutInfo.place(x=24, y=269)

    buttonDeleteFiles = tk.Button(tabAbout, text="Delete Files", font=("Tahoma", 30), width=34, height=2)
    buttonDeleteFiles.place(x=22, y=392)

    # Persistence
    readStates()
    # Majikoi TODO
    # Majikoi S TODO

    # Majikoi A-1
    if int(mA1States[0]) == 0:
        mA1BenkiVal.set(0)
    else:
        mA1BenkiVal.set(1)

    if int(mA1States[1]) == 0:
        mA1AzumiVal.set(0)
    else:
        mA1AzumiVal.set(1)

    if int(mA1States[2]) == 0:
        mA1SayakaVal.set(0)
    else:
        mA1SayakaVal.set(1)

    # Majikoi A-2
    if int(mA2States[0]) == 0:
        mA2MonshiroVal.set(0)
    else:
        mA2MonshiroVal.set(1)

    if int(mA2States[1]) == 0:
        mA2AiessVal.set(0)
    else:
        mA2AiessVal.set(1)
    
    if int(mA2States[2]) == 0:
        mA2SeisoVal.set(0)
    else:
        mA2SeisoVal.set(1)
    
    # Majikoi A-3 TODO
    # Majikoi A-4 TODO
    # Majikoi A-5 TODO

    root.protocol("WM_DELETE_WINDOW", writeStates)
    root.mainloop()

init()