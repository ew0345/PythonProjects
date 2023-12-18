import tkinter as tk

def init():
    root = tk.Tk()
    # Set Window Size
    root.geometry("253x215")
    # Set Window Title
    root.title("Launcher")

    # Menubar
    menu = tk.Menu(root)
    
    menuFile = tk.Menu(menu, tearoff=0)
    menuFile.add_command(label="Exit", command=root.quit)

    menu.add_cascade(label="File", menu=menuFile)
    root.config(menu=menu)

    root.mainloop()
init()