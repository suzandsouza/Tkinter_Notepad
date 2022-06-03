from logging import root
from msilib.schema import File
from tkinter import *
from tkinter.messagebox import showinfo
from unittest import TestCase
from click import open_file
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter.filedialog import askopenfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file = askopenfilename(defaultextension=".txt",
    filetypes=[("All Files", "*.*"),
    ("Text Documents","*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

    TextArea.delete(1.0,END)
    #1.0 -->1st line zeroth character

def openFile():
    global file

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #Save as a new filee
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
    
    else:
        #Save a new file
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitcommand():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def highlight():
    TextArea.event_generate("<<Highlight>>")

def edit():
    pass

def about():
    showinfo("NOTEPAD","Notepad by Suzan")

# def highlight_text(self):
#     #if no text is selected then tk.tclerror
#     try:
#         self.text.tag_add("start","sel.first","sel.last")
#     except tk.TclError:
#         pass
if __name__=='__main__':
    #Basoc tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("700x600")
    root['bg'] = 'black'
    
    # #this will add highlight button iin te wondow
    # bold_btn = tk.Button(self.toolbar,)
    #Add TextArea
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH,expand=True)

    #creating menu bar
    MenuBar = Menu(root)
    #File menu starts
    FileMenu = Menu(MenuBar, tearoff=0)
    
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To open an already existing file
    FileMenu.add_command(label="Open", command=openFile)

    #To save the current file

    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitcommand)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    #File menu ends

    #Edit menu starts
    EditMenu = Menu(MenuBar,tearoff=0)
    #To give a feature of cut, copy, paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    EditMenu.add_command(label="Highlight",command=highlight)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    #Edit menu ends
    #Help menu starts
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command = about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    #Help menu ends


    root.config(menu = MenuBar)    

    cursors = ["mouse"]
    #adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview,cursor=cursors)
    TextArea.config(yscrollcommand=Scroll.set)
    #end of scroll bar addition
    root.mainloop()