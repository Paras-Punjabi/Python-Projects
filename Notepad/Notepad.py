from tkinter import *
import os
from tkinter import messagebox,filedialog
from webbrowser import open_new_tab
import datetime

class Notepad:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.resizable(False,False)
        self.root.title("Untitled-Notepad")
        self.inputText = None
        self.addMenuBar()
        self.addTextarea()
        self.root.mainloop()

    def createNewFile(self):
        self.root.title("Untitled - Notedpad")
        self.inputText.delete("1.0",END)
    
    def openFile(self):
        path = filedialog.askopenfile(title="Select your File",filetypes=(('Text Files', '*.txt'),
        ('All Files', '*.*')),initialdir="/")
        if(path):
            file = open(path.name,mode="r")
            text = file.read()
            self.inputText.insert("1.0",text)
            file.close()
            self.root.title(os.path.splitext(os.path.basename(path.name))[0] + " - Notepad")

    def saveFile(self):
        path = filedialog.asksaveasfilename(title="Select your Directory",filetypes=( ('Text Files', '*.txt'),
        ('All Files', '*.*')), initialdir="/")
        if path:
            file = open(path,mode="w")
            file.write(self.inputText.get("1.0",END))
            file.close()
            self.root.title(os.path.splitext(os.path.basename(path))[0] + " - Notepad")
    
    def saveAsFile(self):
        path = filedialog.askopenfile(title="Select your File",filetypes=(("Text Files",".txt"),("All Files",".")),initialdir="/")
        file = open(path.name,mode="w")
        file.write(self.inputText.get("1.0",END))
        file.close()
    
    def runPython(self):
        file = open("python_program_using_tkinter_by_paras_punjabi.py",mode="w")
        file.write(self.inputText.get("1.0",END))
        file.close()
        os.system("python python_program_using_tkinter_by_paras_punjabi.py")
        os.remove("python_program_using_tkinter_by_paras_punjabi.py")
    
    def runJS(self):
        file = open("javascript_program_using_tkinter_by_paras_punjabi.js",mode="w")
        file.write(self.inputText.get("1.0",END))
        file.close()
        os.system("node javascript_program_using_tkinter_by_paras_punjabi.js")
        os.remove("javascript_program_using_tkinter_by_paras_punjabi.js")
    
    def searchGoogle(self):
        try:
            text = self.inputText.get(SEL_FIRST,SEL_LAST)
            open_new_tab(f"https://www.google.com/search?q={text}")
        except:
            messagebox.showwarning(title="Warning",message="First select some text")
    
    def deleteText(self):
        try:
           self.inputText.delete(SEL_FIRST,SEL_LAST)
        except:
            messagebox.showwarning(title="Warning",message="First select some text")
    
    def addMenuBar(self):
        menu = Menu(self.root)
        file = Menu(menu,tearoff=False)
        about = Menu(menu,tearoff=False)
        edit = Menu(menu,tearoff=False)
        run = Menu(menu,tearoff=False)
        social = Menu(menu,tearoff=False)

        menu.add_cascade(label="File",menu=file)
        menu.add_cascade(label="Edit",menu=edit)
        menu.add_cascade(label="Social Media",menu=social)
        menu.add_cascade(label="Run",menu=run)
        menu.add_cascade(label="Help",menu=about)

        file.add_cascade(label="New",command=self.createNewFile)
        file.add_cascade(label="New Window",command=lambda:Notepad())
        file.add_cascade(label="Open",command=self.openFile)
        file.add_separator()
        file.add_cascade(label="Save",command=self.saveFile)
        file.add_cascade(label="Save As",command=self.saveAsFile)
        file.add_separator()
        file.add_cascade(label="Exit",command=self.root.destroy)

        edit.add_cascade(label="Cut",command=lambda:self.inputText.event_generate("<<Cut>>"))
        edit.add_cascade(label="Copy",command=lambda:self.inputText.event_generate("<<Copy>>"))
        edit.add_cascade(label="Paste",command=lambda:self.inputText.event_generate("<<Paste>>"))
        edit.add_cascade(label="Delete",command=self.deleteText)
        edit.add_separator()
        edit.add_cascade(label="Search Chrome",command=self.searchGoogle)
        edit.add_separator()
        edit.add_cascade(label="Time/Date",command=lambda:self.inputText.insert(END,datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')))

        about.add_cascade(label="About Notepad",command=lambda:messagebox.askokcancel(title="About",message="This is a notepad made using Tkinter in Python by Paras Punjabi"))

        social.add_cascade(label="Instagram",command=lambda:open_new_tab("https://www.instagram.com"))
        social.add_cascade(label="Facebook",command=lambda:open_new_tab("https://www.facebook.com"))
        social.add_cascade(label="GitHub",command=lambda:open_new_tab("https://www.github.com/Paras-Punjabi"))

        run.add_cascade(label="Run Python",command=self.runPython)
        run.add_cascade(label="Run Javascript(Node Js)",command=self.runJS)

        self.root.config(menu=menu)
    
    def addTextarea(self):
        self.inputText = Text(self.root,width=self.root.winfo_screenmmwidth(),height=self.root.winfo_screenmmheight(),font=("Lucida Console",15,"bold"))
        self.inputText.pack()

if __name__ == '__main__':
    Notepad()
    
   
    