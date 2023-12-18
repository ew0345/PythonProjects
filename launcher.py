import tkinter as tk
import subprocess

def open(app):
    # What application to open when a button is clicked
    apps = {0: "scc.py", 1: "archcalc.py"}
    try:
        subprocess.Popen(["py", apps[app]])
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
    # Application Icon
    root.iconbitmap("./images/Icon3.ico")

    # Images
    image = tk.PhotoImage(file="./images/Icon3.png")

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

    root.mainloop()

init()