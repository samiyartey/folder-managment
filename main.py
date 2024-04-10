from tkinter.filedialog import askdirectory
import tkinter as tkp
from customtkinter import *
import os

root = CTk()
root.title("folder managment")

def create():
    createe = open(filepath.get(),"w")
def search():
    global musiclist
    for item in musiclist:
        if item.endswith(formatt.get()):
            i = 0
            playlist.insert(i, item)
            i = i + 1


tab = CTkTabview(root)
tab.pack()
finder = tab.add("file finder")
playlist = tkp.Listbox(finder)
playlist.pack(fill="x")
directory = askdirectory()
os.chdir(directory)
musiclist = os.listdir(directory)
formatt = CTkEntry(finder)
formatt.pack()
searchbut = CTkButton(finder, text="search", command=search)
searchbut.pack()
openbut = CTkButton(finder,text="open",command=lambda:os.startfile(playlist.get(tkp.ACTIVE)))
openbut.pack()
creator = tab.add("file creator")
filepath = CTkEntry(creator)
filepath.pack()
createbut = CTkButton(creator,text="create",command=create)
createbut.pack()
dircreate = tab.add("create folder")
folpath = CTkEntry(dircreate)
folpath.pack()
createbut = CTkButton(dircreate,text="create",command=lambda:os.mkdir(folpath.get()))
createbut.pack()

root.mainloop()
