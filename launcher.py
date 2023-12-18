import tkinter as tk
import subprocess

def open(app):
    # What application to open when a button is clicked
    apps = {0: "scc.py", 1: "archcalc.py", 2: "majikoi.py"}
    try:
        subprocess.Popen(["py", "apps/"+apps[app]])
        root.quit()
    except KeyError:
        print(f"{app} is an invalid application id.")

def init():
    global root
    root = tk.Tk()
    # Set Window Size
    root.geometry("253x215")
    # Set Window Title
    root.title("Launcher")
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
    menuFile.add_command(label="Exit", command=root.quit)

    menu.add_cascade(label="File", menu=menuFile)
    root.config(menu=menu)

    # Labels
    labelImage = tk.Label(root, image=image)
    labelImage.place(x=150, y=35)

    labelMadeBy = tk.Label(root, text="Made By Ew0345")
    labelMadeBy.place(x=150, y=89)

    # Buttons
    buttonSCC = tk.Button(root, text="Sheer Cold Calculator", width=18, command=lambda: open(0))
    buttonSCC.place(x=10, y=30)

    buttonArch = tk.Button(root, text="Arch Tome Calculator", width=18, command=lambda: open(1))
    buttonArch.place(x=10, y=60)

    buttonMaji = tk.Button(root, text="Majikoi Route Tracker", width=18, command=lambda: open(2))
    buttonMaji.place(x=10, y=90)

    root.mainloop()

init()