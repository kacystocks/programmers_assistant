from tkinter import *
import ctypes
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.mWindow = tkinter.Tk()
        self.mFrame = Frame(self.mWindow, width=300, height=65)

# tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")
# yesBtn = tkinter.Button(top_frame, text = "YES", fg = "green").pack()
# tkinter.Label(window, text = "Welcome to your SABER command line! Say one of these commands to see something cool. Waiting for commands...", fg = "white", bg = "black").pack(fill = "x")
        
    def ErrorWindow(self,message):
        self.mWindow.title("ERROR")
        x = self.mWindow.winfo_screenwidth()
        y = self.mWindow.winfo_screenheight()
        self.mWindow.geometry("300x65+{0}+{1}".format(int(x/2 - 150),int(y/2 - 32)))
        # set_to_foreground = ctypes.windll.user32.SetForegroundWindow
        # tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")
        tkinter.Label(self.mWindow, text = message, fg = "white", bg = "black").pack(fill = "x", pady = 20, ipady = 10)
        tkinter.Button(self.mWindow, text = "Ok", command = self.mWindow.quit).pack()
        # set_to_foreground(self.mWindow.winfo_id())
        #def end(event):
        #    self.mWindow.destory()

        #self.mWindow.bind("<Enter>", end)
        self.mFrame.pack()
        
        self.mWindow.mainloop()

# Error, message, yes/no

def main():
    new = GUI()
    new.ErrorWindow("You done effed up.")

main()
