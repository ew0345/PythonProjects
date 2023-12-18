import tkinter as tk
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
    root.geometry("253x215")
    # Set Window Title
    root.title("Tome Calc")

    root.mainloop()

init()