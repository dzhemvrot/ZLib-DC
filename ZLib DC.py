import zlib
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from collections import deque

#with open(r"C:\Users\Admin\Desktop\scene_j_a2.rsd", 'rb') as myfile:
#    f = myfile.read()
#z = open(r"C:\Users\Admin\Desktop\scene_j_a2.rsd.txt", "ab")
#print("\nDecompressed String")
#z.write(zlib.decompress(f))

class Window:

    def __init__(self, master):
        self.master = master
        self.master.option_add("*Font", "Verdana 12")
 
        self.Main = Frame(self.master)
 
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
 
        self.L1 = Label(self.Main, text = "ZLib DC - ZLib De- and Compresser")
        self.L1.pack(padx = 5, pady = 5)

        self.menu = Menu(self.Main)
        self.menu.add_command(label = "Decompress", command = self.Decompress)
        self.menu.add_command(label = "Compress", command = self.Compress)
        self.menu.add_command(label = "About", command = self.About)
        self.menu.option_add("*Font", "Verdana 12")
 
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Decompress", width = 12, command = self.Decompress)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
        self.B1.option_add("*Font", "Verdana 12")

        self.B2 = Button(self.Main, text = "Compress", width = 12, command = self.Compress)
        self.B2.pack(padx = 5, pady = 5, side = RIGHT)
        self.B2.option_add("*Font", "Verdana 12")
 
        self.Main.pack(padx = 5, pady = 5)

    
    def Compress(self):
        ftypes = [('Txt file', '.txt')]
        filename = fd.askopenfilename(filetypes=ftypes)
        with open(filename, 'rb') as myfile:
            f = myfile.read()
        newfilename = filename.replace('.txt', '')
        z = open(newfilename, "ab")
        print("Compressed String")
        z.write(zlib.compress(f, level=9))
        tk.messagebox.showinfo(title='Success!', message='File compressed successfully!')

    def Decompress(self):
        ftypes = [('All files', '*')]
        filename = fd.askopenfilename(filetypes=ftypes)
        with open(filename, 'rb') as myfile:
            f = myfile.read()
        newfilename = filename + ".txt"
        z = open(newfilename, "ab")
        print("Decompressed String")
        z.write(zlib.decompress(f))
        tk.messagebox.showinfo(title='Success!', message='File decompressed successfully!')

    def About(self):
        tk.messagebox.showinfo(title='About', message='''This is a program to compress and decompress files, using Z-Library.

Program authors: dzhemvrot; osaten''')

root = Tk()
root.resizable(False, False)
window = Window(root)
root.title(u'ZLib DC')
root.mainloop()
