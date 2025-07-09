import os
import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import messagebox

def returnToLauncher():
    try:
        subprocess.Popen(["py", "launcher.py"])
        root.quit()
    except Exception as e:
        print(f"Failed to launch launcher.py: {e}")

def deleteFiles():
    mbDeleteFile = messagebox.askyesno("Delete Files", "Do you want to delete the files? Program will exit after deleting files.")
    
    if mbDeleteFile == True:
        # Delete files
        files = [m1State, mSState, mA1State, mA2State, mA3State, mA4State, mA5State]

        for i in files:
            if os.path.isfile(i):
                os.remove(i)

        clearStates()
        root.quit()


def clearStates():
    # Majikoi game variables
    checkboxes = [mMomoyo, mChris, mMiyako, mYukie, mKazuko, mKojima, mChika, mMoro, mCapt, mGakuto, mHermitCrabs, mNoRelationship, mMayo, mTutorialRoom, mAgave, mMomoyoAfter, mMiyakoAfter, mYukieAfter, mKazukoAfter, mSCommon, mSMonshiro, mSMonshiroCont, mSMargit, mSMargitCont, mSTsubame, mSTsubameCont, mSTsubameF1, mSTsubameF2, mSIyo, mSShima, mSMaids, mSKazamaFam, mSTatsuko, mSYumiko, mSDevotedCrabs, mSMiyakoAF1, mSMiyakoAF2, mSMiyakoAF3, mSChousokabe, mSKokoro, mSNoRelationship, mSKosugi, mSKosugiCont, mSChildhood, mSKoyuki, mSKoyukiF, mSTakae, mSMonshiroAfter, mSKazukoS, mSMomoyoS, mSMiyakoS, mSYukieS, mSChrisS, mSTsubameAF1, mSTsubameAF2, mSHermitCrabsS, mSAgaveAfter, mA1BenkiVal, mA1AzumiVal, mA1SayakaVal, mA2MonshiroVal, mA2AiessVal, mA2SeisoVal, mA3LeeVal, mA3StacyVal, mA3TsubameVal, mA4LinVal, mA4HomuraVal, mA5YoshitsuneVal, mA5TakaeVal, mA5MargitVal]

    for i, var in enumerate(checkboxes):
        var.set(0)

def writeStates(ret):
    # Majikoi
    mVars = [mMomoyo, mChris, mMiyako, mYukie, mKazuko, mKojima, mChika, mMoro, mCapt, mGakuto, mHermitCrabs, mNoRelationship, mMayo, mTutorialRoom, mAgave, mMomoyoAfter, mMiyakoAfter, mYukieAfter, mKazukoAfter]

    for i, var in enumerate(mVars):
        m1States[i] = 0 if var.get() == 0 else 1

    with open(m1State, "w") as f:
        for item in m1States:
            f.write("%s\n" % item)

    # Majikoi S
    mSVars = [mSCommon, mSMonshiro, mSMonshiroCont, mSMargit, mSMargitCont, mSTsubame, mSTsubameCont, mSTsubameF1, mSTsubameF2, mSIyo, mSShima, mSMaids, mSKazamaFam, mSTatsuko, mSYumiko, mSDevotedCrabs, mSMiyakoAF1, mSMiyakoAF2, mSMiyakoAF3, mSChousokabe, mSKokoro, mSNoRelationship, mSKosugi, mSKosugiCont, mSChildhood, mSKoyuki, mSKoyukiF, mSTakae, mSMonshiroAfter, mSKazukoS, mSMomoyoS, mSMiyakoS, mSYukieS, mSChrisS, mSTsubameAF1, mSTsubameAF2, mSHermitCrabsS, mSAgaveAfter]

    for i, var in enumerate(mSVars):
        mSStates[i] = 0 if var.get() == 0 else 1
    
    with open(mSState, "w") as f:
        for item in mSStates:
            f.write("%s\n" % item)
    
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

    # Majikoi A-5
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

def readStates():
    # Majikoi Routes Directory
    dirHome = os.path.expanduser("~")
    dirMaji = "MajikoiRoutes"
    global dirPath; dirPath = os.path.join(dirHome, dirMaji)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    # Majikoi States Files
    global m1State; m1State = dirPath+"/m1State.txt"
    global mSState; mSState = dirPath+"/mSState.txt"
    global mA1State; mA1State = dirPath+"/mA1State.txt"
    global mA2State; mA2State = dirPath+"/mA2State.txt"
    global mA3State; mA3State = dirPath+"/mA3State.txt"
    global mA4State; mA4State = dirPath+"/mA4State.txt"
    global mA5State; mA5State = dirPath+"/mA5State.txt"

    # Handle State files

    # Majikoi
    global m1States
    if not os.path.isfile(m1State):
        with open(m1State, "w") as f:
            f.write("0\n" * 19)
        with open(m1State, "r") as f:
            m1States = [line.strip() for line in f.readlines()]
    elif os.path.isfile(m1State):
        with open(m1State, "r") as f:
            m1States = [line.strip() for line in f.readlines()]

    mVars = [mMomoyo, mChris, mMiyako, mYukie, mKazuko, mKojima, mChika, mMoro, mCapt, mGakuto, mHermitCrabs, mNoRelationship, mMayo, mTutorialRoom, mAgave, mMomoyoAfter, mMiyakoAfter, mYukieAfter, mKazukoAfter]

    for i, var in enumerate(mVars):
        var.set(0 if int(m1States[i]) == 0 else 1)
    
    # Majikoi S
    global mSStates
    if not os.path.isfile(mSState):
        with open(mSState, "w") as f:
            f.write("0\n" * 38)
        with open(mSState, "r") as f:
            mSStates = [line.strip() for line in f.readlines()]
    elif os.path.isfile(mSState):
        with open(mSState, "r") as f:
            mSStates = [line.strip() for line in f.readlines()]
    
    mSVars = [mSCommon, mSMonshiro, mSMonshiroCont, mSMargit, mSMargitCont, mSTsubame, mSTsubameCont, mSTsubameF1, mSTsubameF2, mSIyo, mSShima, mSMaids, mSKazamaFam, mSTatsuko, mSYumiko, mSDevotedCrabs, mSMiyakoAF1, mSMiyakoAF2, mSMiyakoAF3, mSChousokabe, mSKokoro, mSNoRelationship, mSKosugi, mSKosugiCont, mSChildhood, mSKoyuki, mSKoyukiF, mSTakae, mSMonshiroAfter, mSKazukoS, mSMomoyoS, mSMiyakoS, mSYukieS, mSChrisS, mSTsubameAF1, mSTsubameAF2, mSHermitCrabsS, mSAgaveAfter]

    for i, var in enumerate(mSVars):
        var.set(0 if int(mSStates[i]) == 0 else 1)

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

    # TTK Style Info
    style = ttk.Style()
    style.configure("Custom.TCheckbutton", font=("Tahoma", 13))
    style.configure("Custom.TButton", font=("Tahoma", 30), padding=(0, 50))

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
    Momoyo = ttk.Checkbutton(tabMaji, text="Momoyo", style="Custom.TCheckbutton", variable=mMomoyo)
    Momoyo.place(x=10, y=49)

    Chris = ttk.Checkbutton(tabMaji, text="Chris", style="Custom.TCheckbutton", variable=mChris)
    Chris.place(x=10, y=75)

    Miyako = ttk.Checkbutton(tabMaji, text="Miyako", style="Custom.TCheckbutton", variable=mMiyako)
    Miyako.place(x=10, y=101)

    Yukie = ttk.Checkbutton(tabMaji, text="Yukie", style="Custom.TCheckbutton", variable=mYukie)
    Yukie.place(x=10, y=127)

    Kazuko = ttk.Checkbutton(tabMaji, text="Kazuko", style="Custom.TCheckbutton", variable=mKazuko)
    Kazuko.place(x=10, y=153)

    Kojima = ttk.Checkbutton(tabMaji, text="Kojima-sensei", style="Custom.TCheckbutton", variable=mKojima)
    Kojima.place(x=166, y=49)

    Chika = ttk.Checkbutton(tabMaji, text="Chika", style="Custom.TCheckbutton", variable=mChika)
    Chika.place(x=166, y=75)

    Moro = ttk.Checkbutton(tabMaji, text="Moro", style="Custom.TCheckbutton", variable=mMoro)
    Moro.place(x=166, y=101)

    Capt = ttk.Checkbutton(tabMaji, text="Capt", style="Custom.TCheckbutton", variable=mCapt)
    Capt.place(x=166, y=127)

    Gakuto = ttk.Checkbutton(tabMaji, text="Gakuto", style="Custom.TCheckbutton", variable=mGakuto)
    Gakuto.place(x=166, y=153)

    HermitCrabs = ttk.Checkbutton(tabMaji, text="Hermit Crabs", style="Custom.TCheckbutton", variable=mHermitCrabs)
    HermitCrabs.place(x=166, y=179)

    NoRelationship = ttk.Checkbutton(tabMaji, text="No Relationship", style="Custom.TCheckbutton", variable=mNoRelationship)
    NoRelationship.place(x=166, y=205)

    Mayo = ttk.Checkbutton(tabMaji, text="Mayo", style="Custom.TCheckbutton", variable=mMayo)
    Mayo.place(x=166, y=231)

    TutorialRoom = ttk.Checkbutton(tabMaji, text="Tutorial Room", style="Custom.TCheckbutton", variable=mTutorialRoom)
    TutorialRoom.place(x=334, y=49)

    Agave = ttk.Checkbutton(tabMaji, text="Agave", style="Custom.TCheckbutton", variable=mAgave)
    Agave.place(x=334, y=75)

    MomoyoAfter = ttk.Checkbutton(tabMaji, text="Momoyo After", style="Custom.TCheckbutton", variable=mMomoyoAfter)
    MomoyoAfter.place(x=491, y=49)

    MiyakoAfter = ttk.Checkbutton(tabMaji, text="Miyako After", style="Custom.TCheckbutton", variable=mMiyakoAfter)
    MiyakoAfter.place(x=491, y=75)

    YukieAfter = ttk.Checkbutton(tabMaji, text="Yukie After", style="Custom.TCheckbutton", variable=mYukieAfter)
    YukieAfter.place(x=491, y=101)

    KazukoAfter = ttk.Checkbutton(tabMaji, text="Kazuko After", style="Custom.TCheckbutton", variable=mKazukoAfter)
    KazukoAfter.place(x=491, y=127)

    # Majikoi S
    # Variables
    global mSCommon; mSCommon = tk.IntVar()
    global mSMonshiro; mSMonshiro = tk.IntVar()
    global mSMonshiroCont; mSMonshiroCont= tk.IntVar()
    global mSMargit; mSMargit = tk.IntVar()
    global mSMargitCont; mSMargitCont = tk.IntVar()
    global mSTsubame; mSTsubame = tk.IntVar()
    global mSTsubameCont; mSTsubameCont = tk.IntVar()
    global mSTsubameF1; mSTsubameF1 = tk.IntVar()
    global mSTsubameF2; mSTsubameF2 = tk.IntVar()
    global mSIyo; mSIyo = tk.IntVar()
    global mSShima; mSShima = tk.IntVar()
    global mSMaids; mSMaids = tk.IntVar()
    global mSKazamaFam; mSKazamaFam = tk.IntVar()
    global mSTatsuko; mSTatsuko = tk.IntVar()
    global mSYumiko; mSYumiko = tk.IntVar()
    global mSDevotedCrabs; mSDevotedCrabs = tk.IntVar()
    global mSMiyakoAF1; mSMiyakoAF1 = tk.IntVar()
    global mSMiyakoAF2; mSMiyakoAF2 = tk.IntVar()
    global mSMiyakoAF3; mSMiyakoAF3 = tk.IntVar()
    global mSChousokabe; mSChousokabe = tk.IntVar()
    global mSKokoro; mSKokoro = tk.IntVar()
    global mSNoRelationship; mSNoRelationship = tk.IntVar()
    global mSKosugi; mSKosugi = tk.IntVar()
    global mSKosugiCont; mSKosugiCont = tk.IntVar()
    global mSChildhood; mSChildhood = tk.IntVar()
    global mSKoyuki; mSKoyuki = tk.IntVar()
    global mSKoyukiF; mSKoyukiF = tk.IntVar()
    global mSTakae; mSTakae = tk.IntVar()
    global mSMonshiroAfter; mSMonshiroAfter = tk.IntVar()
    global mSKazukoS; mSKazukoS = tk.IntVar()
    global mSMomoyoS; mSMomoyoS = tk.IntVar()
    global mSMiyakoS; mSMiyakoS = tk.IntVar()
    global mSYukieS; mSYukieS = tk.IntVar()
    global mSChrisS; mSChrisS = tk.IntVar()
    global mSTsubameAF1; mSTsubameAF1 = tk.IntVar()
    global mSTsubameAF2; mSTsubameAF2 = tk.IntVar()
    global mSHermitCrabsS; mSHermitCrabsS = tk.IntVar()
    global mSAgaveAfter; mSAgaveAfter = tk.IntVar()

    # Labels
    labelSMainRoutes = tk.Label(tabMajiS, text="Main Routes", font=("Tahoma", 15))
    labelSMainRoutes.place(x=10, y=11)

    labelSSubRoutes = tk.Label(tabMajiS, text="Sub Routes", font=("Tahoma", 15))
    labelSSubRoutes.place(x=405, y=11)

    labelSHiddenRoutes = tk.Label(tabMajiS, text="Hidden Routes", font=("Tahoma", 15))
    labelSHiddenRoutes.place(x=10, y=261)

    labelSAfterRoutes = tk.Label(tabMajiS, text="After Routes", font=("Tahoma", 15))
    labelSAfterRoutes.place(x=385, y=261)

    # Checkbuttons
    sCommon = ttk.Checkbutton(tabMajiS, text="2nd Year 1st Semester", style="Custom.TCheckbutton", variable=mSCommon)
    sCommon.place(x=10, y=49)

    sMonshiro = ttk.Checkbutton(tabMajiS, text="Monshiro", style="Custom.TCheckbutton", variable=mSMonshiro)
    sMonshiro.place(x=10, y=75)

    sMonshiroCont = ttk.Checkbutton(tabMajiS, text="Monshiro Continued", style="Custom.TCheckbutton", variable=mSMonshiroCont)
    sMonshiroCont.place(x=10, y=101)

    sMargit = ttk.Checkbutton(tabMajiS, text="Margit", style="Custom.TCheckbutton", variable=mSMargit)
    sMargit.place(x=10, y=127)

    sMargitCont = ttk.Checkbutton(tabMajiS, text="Margit Continued", style="Custom.TCheckbutton", variable=mSMargitCont)
    sMargitCont.place(x=10, y=153)

    sTsubame = ttk.Checkbutton(tabMajiS, text="Tsubame", style="Custom.TCheckbutton", variable=mSTsubame)
    sTsubame.place(x=10, y=179)

    sTsubameF1 = ttk.Checkbutton(tabMajiS, text="Future Where Tsubame Takes the Lead", style="Custom.TCheckbutton", variable=mSTsubameF1)
    sTsubameF1.place(x=10, y=205)

    sTsubameF2 = ttk.Checkbutton(tabMajiS, text="Future Where Yamato Takes the Lead", style="Custom.TCheckbutton", variable=mSTsubameF2)
    sTsubameF2.place(x=10, y=231)

    sIyo = ttk.Checkbutton(tabMajiS, text="Iyo", style="Custom.TCheckbutton", variable=mSIyo)
    sIyo.place(x=308, y=49)

    sShima = ttk.Checkbutton(tabMajiS, text="Future with Shima", style="Custom.TCheckbutton", variable=mSShima)
    sShima.place(x=308, y=152)

    sMaids = ttk.Checkbutton(tabMajiS, text="Future with the Maids", style="Custom.TCheckbutton", variable=mSMaids)
    sMaids.place(x=308, y=178)

    sKazamaFam = ttk.Checkbutton(tabMajiS, text="Future with the Kazama Family", style="Custom.TCheckbutton", variable=mSKazamaFam)
    sKazamaFam.place(x=503, y=74)

    sTatsuko = ttk.Checkbutton(tabMajiS, text="Tatsuko", style="Custom.TCheckbutton", variable=mSTatsuko)
    sTatsuko.place(x=308, y=74)

    sYumiko = ttk.Checkbutton(tabMajiS, text="Yumiko", style="Custom.TCheckbutton", variable=mSYumiko)
    sYumiko.place(x=308, y=100)

    sDevotedCrabs = ttk.Checkbutton(tabMajiS, text="Future Devoted to Hermit Crabs", style="Custom.TCheckbutton", variable=mSDevotedCrabs)
    sDevotedCrabs.place(x=503, y=100)

    sMiyakoAF1 = ttk.Checkbutton(tabMajiS, text="Another Future with Miyako 1", style="Custom.TCheckbutton", variable=mSMiyakoAF1)
    sMiyakoAF1.place(x=503, y=126)

    sMiyakoAF2 = ttk.Checkbutton(tabMajiS, text="Another Future with Miyako 2", style="Custom.TCheckbutton", variable=mSMiyakoAF2)
    sMiyakoAF2.place(x=503, y=152)

    sMiyakoAF3 = ttk.Checkbutton(tabMajiS, text="Another Future with Miyako 3", style="Custom.TCheckbutton", variable=mSMiyakoAF3)
    sMiyakoAF3.place(x=503, y=178)

    sChousokabe = ttk.Checkbutton(tabMajiS, text="Future with Chousokabe", style="Custom.TCheckbutton", variable=mSChousokabe)
    sChousokabe.place(x=405, y=204)

    sKokoro = ttk.Checkbutton(tabMajiS, text="Kokoro", style="Custom.TCheckbutton", variable=mSKokoro)
    sKokoro.place(x=308, y=126)

    sNoRelationship = ttk.Checkbutton(tabMajiS, text="Future without a Relationship", style="Custom.TCheckbutton", variable=mSNoRelationship)
    sNoRelationship.place(x=503, y=48)

    sKosugi = ttk.Checkbutton(tabMajiS, text="Kosugi", style="Custom.TCheckbutton", variable=mSKosugi)
    sKosugi.place(x=10, y=299)

    sKosugiCont = ttk.Checkbutton(tabMajiS, text="Future with Kosugi Continued", style="Custom.TCheckbutton", variable=mSKosugiCont)
    sKosugiCont.place(x=10, y=325)

    sChildhood = ttk.Checkbutton(tabMajiS, text="Childhood", style="Custom.TCheckbutton", variable=mSChildhood)
    sChildhood.place(x=10, y=351)

    sKoyuki = ttk.Checkbutton(tabMajiS, text="Koyuki", style="Custom.TCheckbutton", variable=mSKoyuki)
    sKoyuki.place(x=10, y=377)

    sKoyukiF = ttk.Checkbutton(tabMajiS, text="Future with Koyuki", style="Custom.TCheckbutton", variable=mSKoyukiF)
    sKoyukiF.place(x=10, y=403)

    sTakae = ttk.Checkbutton(tabMajiS, text="Future Where You're An Acquaintance of Takae", style="Custom.TCheckbutton", variable=mSTakae)
    sTakae.place(x=10, y=429)

    sMonshiroAfter = ttk.Checkbutton(tabMajiS, text="Monshiro After", style="Custom.TCheckbutton", variable=mSMonshiroAfter)
    sMonshiroAfter.place(x=385, y=301)

    sKazukoAfter = ttk.Checkbutton(tabMajiS, text="Kazuko S After", style="Custom.TCheckbutton", variable=mSKazukoS)
    sKazukoAfter.place(x=385, y=327)

    sMomoyoAfter = ttk.Checkbutton(tabMajiS, text="Momoyo S After", style="Custom.TCheckbutton", variable=mSMomoyoS)
    sMomoyoAfter.place(x=385, y=353)

    sMiyakoAfter = ttk.Checkbutton(tabMajiS, text="Miyako S After", style="Custom.TCheckbutton", variable=mSMiyakoS)
    sMiyakoAfter.place(x=385, y=379)

    sYukieAfter = ttk.Checkbutton(tabMajiS, text="Yukie S After", style="Custom.TCheckbutton", variable=mSYukieS)
    sYukieAfter.place(x=385, y=405)

    sChrisAfter = ttk.Checkbutton(tabMajiS, text="Chris After + S After", style="Custom.TCheckbutton", variable=mSChrisS)
    sChrisAfter.place(x=533, y=299)

    sTsubameAF1 = ttk.Checkbutton(tabMajiS, text="Future with Tsubame 1 After", style="Custom.TCheckbutton", variable=mSTsubameAF1)
    sTsubameAF1.place(x=533, y=351)

    sTsubameAF2 = ttk.Checkbutton(tabMajiS, text="Future with Tsubame 2 After", style="Custom.TCheckbutton", variable=mSTsubameAF2)
    sTsubameAF2.place(x=533, y=377)

    sHermitCrabsS = ttk.Checkbutton(tabMajiS, text="Future with Hermit Crabs S After", style="Custom.TCheckbutton", variable=mSHermitCrabsS)
    sHermitCrabsS.place(x=533, y=403)

    sAgaveAfter = ttk.Checkbutton(tabMajiS, text="Agave After", style="Custom.TCheckbutton", variable=mSAgaveAfter)
    sAgaveAfter.place(x=533, y=325)

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
    mA1Benki = ttk.Checkbutton(tabA1, text="Completed", style="Custom.TCheckbutton", variable=mA1BenkiVal)
    mA1Benki.place(x=8, y=34)

    mA1Azumi = ttk.Checkbutton(tabA1, text="Completed", style="Custom.TCheckbutton", variable=mA1AzumiVal)
    mA1Azumi.place(x=147, y=34)
 
    mA1Sayaka = ttk.Checkbutton(tabA1, text="Completed", style="Custom.TCheckbutton", variable=mA1SayakaVal)
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
    mA2Monshiro = ttk.Checkbutton(tabA2, text="Completed", style="Custom.TCheckbutton", variable=mA2MonshiroVal)
    mA2Monshiro.place(x=8, y=34)

    mA2Aiess = ttk.Checkbutton(tabA2, text="Completed", style="Custom.TCheckbutton", variable=mA2AiessVal)
    mA2Aiess.place(x=147, y=34)

    mA2Seiso = ttk.Checkbutton(tabA2, text="Completed", style="Custom.TCheckbutton", variable=mA2SeisoVal)
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
    mA3Lee = ttk.Checkbutton(tabA3, text="Completed", style="Custom.TCheckbutton", variable=mA3LeeVal)
    mA3Lee.place(x=8, y=34)
    
    mA3Stacy = ttk.Checkbutton(tabA3, text="Completed", style="Custom.TCheckbutton", variable=mA3StacyVal)
    mA3Stacy.place(x=147, y=34)

    mA3Tsubame = ttk.Checkbutton(tabA3, text="Completed", style="Custom.TCheckbutton", variable=mA3TsubameVal)
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
    mA4Lin = ttk.Checkbutton(tabA4, text="Completed", style="Custom.TCheckbutton", variable=mA4LinVal)
    mA4Lin.place(x=8, y=34)

    mA4Homura = ttk.Checkbutton(tabA4, text="Complete", style="Custom.TCheckbutton", variable=mA4HomuraVal)
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
    mA5Yoshitsune = ttk.Checkbutton(tabA5, text="Completed", style="Custom.TCheckbutton", variable=mA5YoshitsuneVal)
    mA5Yoshitsune.place(x=8, y=34)

    mA5Takae = ttk.Checkbutton(tabA5, text="Completed", style="Custom.TCheckbutton", variable=mA5TakaeVal)
    mA5Takae.place(x=147, y=34)

    mA5Margit = ttk.Checkbutton(tabA5, text="Completed", style="Custom.TCheckbutton", variable=mA5MargitVal)
    mA5Margit.place(x=269, y=34)
    
    # About
    # Image
    try: 
        image = tk.PhotoImage(file="images/Icon3.png")
    except tk.TclError:
        image = tk.PhotoImage()

    # Labels
    labelImage = tk.Label(tabAbout, image=image)
    labelImage.place(x=249, y=13)

    labelMadeBy = tk.Label(tabAbout, text="Made By Ew0345", font=("Tahoma", 14))
    labelMadeBy.place(x=310, y=30)

    labelGithub = tk.Label(tabAbout, text="Github: https://www.github.com/ew0345", font=("Tahoma", 14))
    labelGithub.place(x=180, y=77)

    labelAboutInfo = tk.Label(tabAbout, text="This program creates a folder and several files in your user home folder\nThe files are all contained within the folder \"MajikoiRoutes\", these can be safely deleted\nHowever deleting these files will reset the state of any checked boxes in the routes tabs.", font=("Tahoma", 14))
    labelAboutInfo.place(x=24, y=269)

    # Buttons
    buttonDeleteFiles = ttk.Button(tabAbout, text="Delete Files", style="Custom.TButton", width=17, command=deleteFiles)
    buttonDeleteFiles.place(x=22, y=392)

    buttonClearStates = ttk.Button(tabAbout, text="Clear States", style="Custom.TButton", width=17, command=clearStates)
    buttonClearStates.place(x=403, y=392)

    # Persistence
    readStates()

    root.protocol("WM_DELETE_WINDOW", lambda: writeStates(False))
    root.mainloop()

init()