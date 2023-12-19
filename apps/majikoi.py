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

def deleteFiles():
    global deleted
    files = [mState, mSState, mA1State, mA2State, mA3State, mA4State, mA5State]

    for i in files:
        if os.path.isfile(i):
            os.remove(i)
            print(f"Removed {i}")
    
    print("Deleted")

    deleted = True

def writeStates(ret):
    if deleted == False:
        # TODO
        # Majikoi TODO
        mVars = [mMomoyo, mChris, mMiyako, mYukie, mKazuko, mKojima, mChika, mMoro, mCapt, mHermitCrabs, mNoRelationship, mMayo, mTutorialRoom, mAgave, mMomoyoAfter, mMiyakoAfter, mYukieAfter, mKazukoAfter]

        for i, var in enumerate(mVars):
            mStates[i] = 0 if var.get() == 0 else 1

        with open(mState, "w") as f:
            for item in mStates:
                f.write("%s\n" % item)
        # Majikoi S TODO
        # Majikoi A-1
        mA1Vars = [mA1BenkiVal, mA1AzumiVal, mA1SayakaVal]
        
        for i, var in enumerate(mA1Vars):
            mA1States[i] = 0 if var.get() == 0 else 1

        with open(mA1State, "w") as f:
            for item in mA1States:
                f.write("%s\n" % item)

        # Majikoi A-2
        mA2Vars = [mA2MonshiroVal, mA2AiessVal, mA2SeisoVal]

        for i, var in enumerate(mA2Vars):
            mA2States[i] = 0 if var.get() == 0 else 1
        
        with open(mA2State, "w") as f:
            for item in mA2States:
                f.write("%s\n" % item)

        # Majikoi A-3
        mA3Vars = [mA3LeeVal, mA3StacyVal, mA3TsubameVal]

        for i, var in enumerate(mA3Vars):
            mA3States[i] = 0 if var.get() == 0 else 1

        with open(mA3State, "w") as f:
            for item in mA3States:
                f.write("%s\n" % item)
        
        # Majikoi A-4 
        mA4Vars = [mA4LinVal, mA4HomuraVal]

        for i, var in enumerate(mA4Vars):
            mA4States[i] = 0 if var.get() == 0 else 1

        with open(mA4State, "w") as f:
            for item in mA4States:
                f.write("%s\n" % item)

        # Majikoi A-5 TODO
        mA5Vars = [mA5YoshitsuneVal, mA5TakaeVal, mA5MargitVal]

        for i, var in enumerate(mA5Vars):
            mA5States[i] = 0 if var.get() == 0 else 1

        with open(mA5State, "w") as f:
            for item in mA5States:
                f.write("%s\n" % item)

        if ret == False:
            root.quit()
        else:
            returnToLauncher()
    else:
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
    global mStates
    if not os.path.isfile(mState):
        with open(mState, "w") as f:
            f.write("0\n" * 19)
        with open(mState, "r") as f:
            mStates = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mState):
        with open(mState, "r") as f:
            mStates = [line.strip() for line in f.readlines()]

    mVars = [mMomoyo, mChris, mMiyako, mYukie, mKazuko, mKojima, mChika, mMoro, mCapt, mHermitCrabs, mNoRelationship, mMayo, mTutorialRoom, mAgave, mMomoyoAfter, mMiyakoAfter, mYukieAfter, mKazukoAfter]

    for i, var in enumerate(mVars):
        var.set(0 if int(mStates[i]) == 0 else 1)
    
    # Majikoi S
    global mSStates
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

    mA1Vars = [mA1BenkiVal, mA1AzumiVal, mA1SayakaVal]

    for i, var in enumerate(mA1Vars):
        var.set(0 if int(mA1States[i]) == 0 else 1)
    
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

    mA2Vars = [mA2MonshiroVal, mA2AiessVal, mA2SeisoVal]

    for i, var in enumerate(mA2Vars):
        var.set(0 if int(mA2States[i]) == 0 else 1)
    
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
    
    mA3Vars = [mA3LeeVal, mA3StacyVal, mA3TsubameVal]

    for i, var in enumerate(mA3Vars):
        var.set(0 if int(mA3States[i]) == 0 else 1)
    
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

    mA4Vars = [mA4LinVal, mA4HomuraVal]

    for i, var in enumerate(mA4Vars):
        var.set(0 if int(mA4States[i]) == 0 else 1)

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

    mA5Vars = [mA5YoshitsuneVal, mA5TakaeVal, mA5MargitVal]

    for i, var in enumerate(mA5Vars):
        var.set(0 if int(mA5States[i]) == 0 else 1)

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
    menuFile.add_command(label="Return to Launcher", command=lambda: writeStates(True))
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

    # Majikoi
    # Variables
    global mMomoyo; mMomoyo = tk.IntVar()
    global mChris; mChris = tk.IntVar()
    global mMiyako; mMiyako = tk.IntVar()
    global mYukie; mYukie = tk.IntVar()
    global mKazuko; mKazuko = tk.IntVar()
    global mKojima; mKojima = tk.IntVar()
    global mChika; mChika = tk.IntVar()
    global mMoro; mMoro = tk.IntVar()
    global mCapt; mCapt = tk.IntVar()
    global mGakuto; mGakuto = tk.IntVar()
    global mHermitCrabs; mHermitCrabs = tk.IntVar()
    global mNoRelationship; mNoRelationship = tk.IntVar()
    global mMayo; mMayo = tk.IntVar()
    global mTutorialRoom; mTutorialRoom = tk.IntVar()
    global mAgave; mAgave = tk.IntVar()
    global mMomoyoAfter; mMomoyoAfter = tk.IntVar()
    global mMiyakoAfter; mMiyakoAfter = tk.IntVar()
    global mYukieAfter; mYukieAfter = tk.IntVar()
    global mKazukoAfter; mKazukoAfter = tk.IntVar()

    # Labels
    labelMainRoutes = tk.Label(tabMaji, text="Main Routes", font=("Tahoma", 15))
    labelMainRoutes.place(x=10, y=11)

    labelSubRoutes = tk.Label(tabMaji, text="Sub Routes", font=("Tahoma", 15))
    labelSubRoutes.place(x=166, y=11)

    labelHiddenRoutes = tk.Label(tabMaji, text="Hidden Routes", font=("Tahoma", 15))
    labelHiddenRoutes.place(x=334, y=11)

    labelAfterRoutes = tk.Label(tabMaji, text="After Routes", font=("Tahoma", 15))
    labelAfterRoutes.place(x=491, y=11)

    # Checkbuttons
    labelMomoyo = tk.Checkbutton(tabMaji, text="Momoyo", font=("Tahoma", 13), variable=mMomoyo)
    labelMomoyo.place(x=10, y=49)

    labelChris = tk.Checkbutton(tabMaji, text="Chris", font=("Tahoma", 13), variable=mChris)
    labelChris.place(x=10, y=75)

    labelMiyako = tk.Checkbutton(tabMaji, text="Miyako", font=("Tahoma", 13), variable=mMiyako)
    labelMiyako.place(x=10, y=101)

    labelYukie = tk.Checkbutton(tabMaji, text="Yukie", font=("Tahoma", 13), variable=mYukie)
    labelYukie.place(x=10, y=127)

    labelKazuko = tk.Checkbutton(tabMaji, text="Kazuko", font=("Tahoma", 13), variable=mKazuko)
    labelKazuko.place(x=10, y=153)

    labelKojima = tk.Checkbutton(tabMaji, text="Kojima-sensei", font=("Tahoma", 13), variable=mKojima)
    labelKojima.place(x=166, y=49)

    labelChika = tk.Checkbutton(tabMaji, text="Chika", font=("Tahoma", 13), variable=mChika)
    labelChika.place(x=166, y=75)

    labelMoro = tk.Checkbutton(tabMaji, text="Moro", font=("Tahoma", 13), variable=mMoro)
    labelMoro.place(x=166, y=101)

    labelCapt = tk.Checkbutton(tabMaji, text="Capt", font=("Tahoma", 13), variable=mCapt)
    labelCapt.place(x=166, y=127)

    labelGakuto = tk.Checkbutton(tabMaji, text="Gakuto", font=("Tahoma", 13), variable=mGakuto)
    labelGakuto.place(x=166, y=153)

    labelHermitCrabs = tk.Checkbutton(tabMaji, text="Hermit Crabs", font=("Tahoma", 13), variable=mHermitCrabs)
    labelHermitCrabs.place(x=166, y=179)

    labelNoRelationship = tk.Checkbutton(tabMaji, text="No Relationship", font=("Tahoma", 13), variable=mNoRelationship)
    labelNoRelationship.place(x=166, y=205)

    labelMayo = tk.Checkbutton(tabMaji, text="Mayo", font=("Tahoma", 13), variable=mMayo)
    labelMayo.place(x=166, y=231)

    labelTutorialRoom = tk.Checkbutton(tabMaji, text="Tutorial Room", font=("Tahoma", 13), variable=mTutorialRoom)
    labelTutorialRoom.place(x=334, y=49)

    labelAgave = tk.Checkbutton(tabMaji, text="Agave", font=("Tahoma", 13), variable=mAgave)
    labelAgave.place(x=334, y=75)

    labelMomoyoAfter = tk.Checkbutton(tabMaji, text="Momoyo After", font=("Tahoma", 13), variable=mMomoyoAfter)
    labelMomoyoAfter.place(x=491, y=49)

    labelMiyakoAfter = tk.Checkbutton(tabMaji, text="Miyako After", font=("Tahoma", 13), variable=mMiyakoAfter)
    labelMiyakoAfter.place(x=491, y=75)

    labelYukieAfter = tk.Checkbutton(tabMaji, text="Yukie After", font=("Tahoma", 13), variable=mYukieAfter)
    labelYukieAfter.place(x=491, y=101)

    labelKazukoAfter = tk.Checkbutton(tabMaji, text="Kazuko After", font=("Tahoma", 13), variable=mKazukoAfter)
    labelKazukoAfter.place(x=491, y=127)

    # Majikoi S TODO
    # Variables
    # Labels
    # Checkbuttons
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

    # Majikoi A-2
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

    # Majikoi A-3
    # Variables
    global mA3LeeVal; mA3LeeVal = tk.IntVar()
    global mA3StacyVal; mA3StacyVal = tk.IntVar()
    global mA3TsubameVal; mA3TsubameVal = tk.IntVar()

    # Labels
    labelLee = tk.Label(tabA3, text="Lee", font=("Tahoma", 13))
    labelLee.place(x=10, y=10)

    labelStacy = tk.Label(tabA3, text="Stacy", font=("Tahoma", 13))
    labelStacy.place(x=147, y=10)

    labelTsubame = tk.Label(tabA3, text="Tsubame", font=("Tahoma", 13))
    labelTsubame.place(x=270, y=10)

    # Checkbuttons
    mA3Lee = tk.Checkbutton(tabA3, text="Completed", font=("Tahoma", 11), variable=mA3LeeVal)
    mA3Lee.place(x=8, y=34)
    
    mA3Stacy = tk.Checkbutton(tabA3, text="Completed", font=("Tahoma", 11), variable=mA3StacyVal)
    mA3Stacy.place(x=147, y=34)

    mA3Tsubame = tk.Checkbutton(tabA3, text="Completed", font=("Tahoma", 11), variable=mA3TsubameVal)
    mA3Tsubame.place(x=269, y=34)

    # Majikoi A-4
    # Variables
    global mA4LinVal; mA4LinVal = tk.IntVar()
    global mA4HomuraVal; mA4HomuraVal = tk.IntVar()

    # Labels
    labelLin = tk.Label(tabA4, text="Lin", font=("Tahoma", 13))
    labelLin.place(x=10, y=10)

    labelHomura = tk.Label(tabA4, text="Homura", font=("Tahoma", 13))
    labelHomura.place(x=147, y=10)

    # Checkbuttons
    mA4Lin = tk.Checkbutton(tabA4, text="Completed", font=("Tahoma", 11), variable=mA4LinVal)
    mA4Lin.place(x=8, y=34)

    mA4Homura = tk.Checkbutton(tabA4, text="Complete", font=("Tahoma", 11), variable=mA4HomuraVal)
    mA4Homura.place(x=147, y=34)

    # Majikoi A-5
    # Variables
    global mA5YoshitsuneVal; mA5YoshitsuneVal = tk.IntVar()
    global mA5TakaeVal; mA5TakaeVal = tk.IntVar()
    global mA5MargitVal; mA5MargitVal = tk.IntVar()

    # Labels
    labelYoshitsune = tk.Label(tabA5, text="Yoshitsune", font=("Tahoma", 13))
    labelYoshitsune.place(x=10, y=10)

    labelTakae = tk.Label(tabA5, text="Takae", font=("Tahoma", 13))
    labelTakae.place(x=147, y=10)

    labelMargit = tk.Label(tabA5, text="Margit After", font=("Tahoma", 13))
    labelMargit.place(x=270, y=10)

    # Checkbuttons
    mA5Yoshitsune = tk.Checkbutton(tabA5, text="Completed", font=("Tahoma", 11), variable=mA5YoshitsuneVal)
    mA5Yoshitsune.place(x=8, y=34)

    mA5Takae = tk.Checkbutton(tabA5, text="Completed", font=("Tahoma", 11), variable=mA5TakaeVal)
    mA5Takae.place(x=147, y=34)

    mA5Margit = tk.Checkbutton(tabA5, text="Completed", font=("Tahoma", 11), variable=mA5MargitVal)
    mA5Margit.place(x=269, y=34)
    
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

    buttonDeleteFiles = tk.Button(tabAbout, text="Delete Files", font=("Tahoma", 30), width=34, height=2, command=deleteFiles)
    buttonDeleteFiles.place(x=22, y=392)

    # Persistence
    readStates()

    root.protocol("WM_DELETE_WINDOW", lambda: writeStates(False))
    root.mainloop()

init()