from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import subprocess

def returnToLauncher():
    try:
        subprocess.Popen(["py", "launcher.py"])
        root.quit()
    except Exception as e:
        print(f"Failed to launch launcher.py: {e}")

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

    # Majikoi
        # TODO
    
    # Majikoi S
        # TODO
    
    # Majikoi A-1
        # TODO

    # Majikoi A-2
        # TODO
    
    # Majikoi A-3
        # TODO
    
    # Majikoi A-4
        # TODO
    
    # Majikoi A-5
        # TODO
    
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

    buttonDeleteFiles = tk.Button(tabAbout, text="Delete Files", font=("Tahoma", 30), width=34)
    buttonDeleteFiles.place(x=22, y=392)
        

    root.mainloop()

init()