import tkinter as tk

def init():
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
    

    root.mainloop()

init()