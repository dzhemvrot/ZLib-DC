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
        self.L1.pack(padx = 5, pady = 0)

        self.menu = Menu(self.Main)
        #self.menu.add_command(label = "Decompress", command = self.Decompress)
        #self.menu.add_command(label = "Compress", command = self.Compress)
        #self.menu.add_command(label = "Debug", command = self.Debug)
        #self.menu.add_command(label = "About", command = self.About)
        #self.menu.add_command(label = "Exit", command = root.destroy) 
         
        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="Compress", command = self.Compress, font = ("Verdana", 10))
        filemenu.add_command(label="Decompress", command = self.Decompress, font = ("Verdana", 10))
        filemenu.add_command(label="Mass compress", command = self.Mcompress, font = ("Verdana", 10))
        filemenu.add_command(label="Mass decompress", command = self.Mdecompress, font = ("Verdana", 10))
        filemenu.add_command(label="Exit", command = root.destroy, font = ("Verdana", 10))
         
        self.menu.add_cascade(label="File",
                             menu=filemenu)
        self.menu.add_command(label = "About", command = self.About)
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Decompress", width = 12, command = self.Decompress)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)

        self.B2 = Button(self.Main, text = "Compress", width = 12, command = self.Compress)
        self.B2.pack(padx = 5, pady = 5, side = RIGHT)

        self.B3 = Button(self.Main, text = "Mass decompress", width = 15, command = self.Mdecompress)
        self.B3.pack(padx = 5, pady = 5, side = LEFT)

        self.B4 = Button(self.Main, text = "Mass compress", width = 15, command = self.Mcompress)
        self.B4.pack(padx = 5, pady = 5, side = RIGHT)

        self.L2 = Label(self.Main, text="""Compression level (1-9)""")
        self.L3 = Label(self.Main, text="""Extension (mass only)""")
        self.T1 = Text(root, height=1, width = 22)
        self.T2 = Text(root, height=1, width = 22)
 
        self.Main.pack(padx = 15, pady = 15)
        #self.L2.pack(padx=5, pady=5)
        self.T1.pack(padx=5, pady=5)
        self.T1.insert(tk.END, "Compression level (1-9)")
        self.T1.bind("<Button-1>", lambda args: self.T1.delete('1.0', END))
        #self.L3.pack(padx=5, pady=5)
        self.T2.pack(padx=5, pady=5)
        self.T2.insert(tk.END, "Extension (mass only)")        
        self.T2.bind("<Button-1>", lambda args: self.T2.delete('1.0', END))

    
    def Compress(self):
        try:
            levelc=int(self.T1.get(1.0, "end-1c"))
        except:
            levelc=9
        #    print("T.get failure")

        if levelc <= 0 and levelc != -1:
            levelc = 1
        if levelc > 9:
            levelc = 9
        
        ftypes = [('All files', '*')]
        filename = fd.askopenfilename(filetypes=ftypes)
        with open(filename, 'rb') as myfile:
            f = myfile.read()
        ftypes = [('All files', '*')]
        newfilename = fd.asksaveasfilename(filetypes=ftypes, initialfile=filename)
        z = open(newfilename, "ab")
        print("Compressed String")
        z.write(zlib.compress(f, level=levelc))
        print(levelc)
        tk.messagebox.showinfo(title='Success!', message='File compressed successfully!')
        myfile.close()

    def Decompress(self):
        ftypes = [('All files', '*')]
        filename = fd.askopenfilename(filetypes=ftypes)
        with open(filename, 'rb') as myfile:
            f = myfile.read()
        ftypes = [('All files', '*')]
        newfilename = fd.asksaveasfilename(filetypes=ftypes, initialfile=filename)
        z = open(newfilename, "ab")
        print("Decompressed String")
        z.write(zlib.decompress(f))
        tk.messagebox.showinfo(title='Success!', message='File decompressed successfully!')
        myfile.close()

    def Mdecompress(self):
        try:
            endi=self.T2.get(1.0, "end-1c")
        except:
            endi=".txt"

        if endi == "" or endi is None:
            endi=".txt"
        if endi.find(".")== -1:
            endi=".txt"
            
        ftypes = [('All files', '*')]
        filename = fd.askopenfilenames(filetypes=ftypes)
        print(filename)
        fnc = len(filename)
        while fnc != 0:
            print(fnc)
            fnz = filename[fnc-1].split(',')
            print(fnz)
            fnz2 = fnz[0]
            with open(fnz2, 'rb') as myfile:
                f = myfile.read()
            #ftypes = [('All files', '*')]
            newfilename = fnz2+endi
            print(newfilename)
            z = open(newfilename, "ab")
            print("Decompressed String")
            z.write(zlib.decompress(f))
            fnc = fnc-1
            myfile.close()
        tk.messagebox.showinfo(title='Success!', message='Files decompressed successfully!')

    def Mcompress(self):
        try:
            endi=self.T2.get(1.0, "end-1c")
        except:
            endi=".zlib"

        if endi == "" or endi is None:
            endi=".zlib"

        if endi.find(".")== -1:
            endi=".zlib"

        try:
            levelc=int(self.T1.get(1.0, "end-1c"))
        except:
            levelc=9
        #    print("T.get failure")

        if levelc <= 0 and levelc != -1:
            levelc = 1
        if levelc > 9:
            levelc = 9
            
        ftypes = [('All files', '*')]
        filename = fd.askopenfilenames(filetypes=ftypes)
        print(filename)
        fnc = len(filename)
        while fnc != 0:
            print(fnc)
            fnz = filename[fnc-1].split(',')
            print(fnz)
            fnz2 = fnz[0]
            with open(fnz2, 'rb') as myfile:
                f = myfile.read()
            #ftypes = [('All files', '*')]
            newfilename = fnz2+endi
            print(newfilename)
            z = open(newfilename, "ab")
            print("Compressed String")
            z.write(zlib.compress(f, level=levelc))
            print(levelc)
            fnc = fnc-1
            myfile.close()
        tk.messagebox.showinfo(title='Success!', message='Files decompressed successfully!')
        

    def About(self):
        tk.messagebox.showinfo(title='About', message='''This is a program to compress and decompress files, using Z-Library.

Program authors: dzhemvrot; osaten
Program version: 3.0
Program restributed using GPL-3.0 license''')

root = Tk()
root.resizable(False, False)
window = Window(root)
root.title(u'ZLib DC')
root.mainloop()
