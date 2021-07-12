import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import sys
import os, subprocess
import pytesseract
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import re
import textile
from pynput.keyboard import Key,Controller,Listener
import keyboard
from collections import Counter
def pyf():
    str="def func():\n\t return\n"
    keyboard.write(str)
def jyf():
    str="void func(){\n\treturn;}\n"
    keyboard.write(str)
def fyf():
    str="for (auto i : v) {\n\n}"
    keyboard.write(str)
def quote():
    keyboard.write('"')
    keyboard.press_and_release("left")
def uote():
    keyboard.write(')')
    keyboard.press_and_release("left")
def ote():
    keyboard.write(']')
    keyboard.press_and_release("left")
def cuote():
    keyboard.write("''")
    keyboard.press_and_release("left")
keyboard.add_hotkey('shift + "',lambda: quote())
keyboard.add_hotkey('shift + (',lambda: uote())
keyboard.add_hotkey('[',lambda: ote())
keyboard.add_hotkey('shift + alt + up',lambda: pythonprogram())
keyboard.add_hotkey('shift + alt + left',lambda: cuote())
keyboard.add_hotkey('shift + ctrl + left',lambda: keyboard.write("for x in :\n"))
keyboard.add_hotkey('shift + ctrl + down',lambda: pyf())
keyboard.add_hotkey('shift + ctrl + /',lambda: jyf())
keyboard.add_hotkey('shift + ctrl + >',lambda: fyf())
filename=None

def newfile():
    filename="untitled"
    text.delete(0.0,END)
    print(text)
def savefile():
    global filename
    if filename=="untitled" or filename==None :
        saveas()

    else:
        print("hey")
        t=text.get(0.0,END)
        f=open(filename,'w')
        f.write(t)
        print(t)
        f.close()
        print("done")
def saveas():
    global filename
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file1 = asksaveasfilename(filetypes=files, defaultextension=files)
    print(file1)
    f = open(file1, "w+")
    t=text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except Exception as e:
        print("error \a",e)

def openfile():

    fname=askopenfilename(filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
    #fname=str(f).split('/').pop().split()[0][:-1]
    print(fname)
    global filename
    filename=fname
    f=open(fname,"r")
    t=str.encode(f.read(),"utf-8")
    text.delete(0.0,END)
    text.insert(0.0,t)
def javaprogram():
    global text
    t=text.get(0.0,END)
    fname=str(t.split("class")[1].split("{")[0]).lstrip()
    print(t)
    f=open(str(fname).rstrip()+".java","w+")
    f.write(t)
    print(fname)
    print(f.read())

    f = open("compy.py", "w+")
    f.write(text.get(0.0, END))
    print(f.read())
    top = tk.Tk()
    top.title("Chatter")

    messages_frame = tk.Frame(top)
    my_msg = tk.StringVar()
    my_msg.set("hello")
    # For the messages to be sent.
    scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
    # Following will contain the messages.
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()
    lis = []

    def runcode():
        global lis
        nonlocal msg_list
        try:
            k = subprocess.check_output("javac " + str(fname).rstrip() + ".java", shell=True)
            if k.decode("utf-8") == "":
                messagebox.showinfo("compile info", "code ran succesfully")
            else:
                messagebox.showinfo("compile info", k.decode("utf-8"))
        except Exception as e:
            messagebox.showerror("compile info", e)
        ''' m = mainWindow(root)
        m.popup()
        tec=m.entryValue()'''
        k = subprocess.Popen("java " + fname,stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # stdout_data = k.communicate(input=str('data_to_write').encode())[0]

        for j in lis:
            time.sleep(0.5)
            k.stdin.write(str.encode(str(j) + '\n'))
        o = k.communicate()[0].decode()
        if o:
            print("output", o)
            messagebox.showinfo("process output", k.communicate()[0].decode())
            msg_list.insert("end", str(o) + "\n")
            msg_list.itemconfigure("end", fg="blue")

        j = k.communicate()[1].decode()
        if j:
            print("error", j)
            messagebox.showinfo("process output", k.communicate()[1].decode())
            msg_list.insert("end", str(j)+"\n")
            msg_list.itemconfigure("end", fg="red")

        lis.clear()

    msg = None

    def send(event=None):
        global lis
        global msg
        nonlocal my_msg
        nonlocal entry_field
        msg = entry_field.get()
        print(msg, my_msg)
        my_msg.set("")
        if msg:
            lis.append(msg)
            print(lis)
            recieve()
        else:
            print("invalid input")

    def recieve():
        global msg
        nonlocal msg_list
        global lis
        if msg:
            msg_list.insert("end", str(msg))

    entry_field = tk.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tk.Button(top, text="Send", command=send)
    send_button.pack()
    run_button = tk.Button(top, text="Run", command=runcode)
    run_button.pack(side=tk.LEFT)
    top.mainloop()

msg=None
lis=[]
def pythonprogram():
    global text
    f = open("compy.py", "w+")
    f.write(text.get(0.0, END))
    print(f.read())
    top = tk.Tk()
    top.title("Chatter")

    messages_frame = tk.Frame(top)
    my_msg = tk.StringVar()
    my_msg.set("hello")
    # For the messages to be sent.
    scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
    # Following will contain the messages.
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()
    lis = []

    def runcode():
        global lis
        k = subprocess.call("cd " + str(os.getcwd()), shell=True)
        k = subprocess.Popen("python compy.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True)
        # stdout_data = k.communicate(input=str('data_to_write').encode())[0]

        for j in lis:
            time.sleep(0.3)
            k.stdin.write(str.encode(str(j) + '\n'))
        o = k.communicate()[0].decode()
        if o:
            print("output", o)
            messagebox.showinfo("process output", k.communicate()[0].decode())
            msg_list.insert("end", str(o)+"\n")
            msg_list.itemconfigure("end", fg="blue")

        j = k.communicate()[1].decode()
        if j:
            print("error", j)
            messagebox.showinfo("process output", k.communicate()[1].decode())
            msg_list.insert("end", str(j)+"\n")
            msg_list.itemconfigure("end", fg="red")

        lis.clear()

    msg=None

    def send(event=None):
        global lis
        global msg
        nonlocal my_msg
        nonlocal entry_field
        msg = entry_field.get()
        print(msg ,my_msg)
        my_msg.set("")
        if msg:
            lis.append(msg)
            print(lis)
            recieve()
        else:
            print("invalid input")

    def recieve():
        global msg
        nonlocal msg_list
        global lis
        if msg:
            msg_list.insert("end", str(msg))


    entry_field = tk.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tk.Button(top, text="Send", command=send)
    send_button.pack()
    run_button = tk.Button(top, text="Run", command=runcode)
    run_button.pack(side=tk.LEFT)
    top.mainloop()
    '''k = subprocess.call("cd "+str(os.getcwd()), shell=True)
    k = subprocess.Popen("python compy.py", shell=True)
    # s=k.communicate(tec.encode("utf-8"))'''

def txtml():
    global text
    t = text.get(0.0, END)
    print(t)
    text.delete(0.0,END)
    text.insert(END,str(textile.textile(t)))


def cprogram():
    f = open("cide.cpp", "w+")
    f.write(text.get(0.0, END))
    print(f.read())
    top = tk.Tk()
    top.title("Chatter")
    messages_frame = tk.Frame(top)
    my_msg = tk.StringVar()
    my_msg.set("hello")
    # For the messages to be sent.
    scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
    # Following will contain the messages.
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()
    lis = []

    def runcode():
        global lis
        m = text.get(0.0, END)
        kis = re.split(r'\s|=|\(', m)
        print(kis)
        c = Counter(m)
        x = c['input']
        print(c)
        k = subprocess.Popen("cd " + str(os.getcwd()), shell=True)
        k = subprocess.Popen("g++ -o cide cide.cpp&cide.exe", shell=True)
        # stdout_data = k.communicate(input=str('data_to_write').encode())[0]
        for j in lis:
            time.sleep(0.5)
            k.stdin.write(str.encode(str(j) + '\n'))
        o = k.communicate()[0].decode()
        if o:
            print("output", o)
            messagebox.showinfo("process output", k.communicate()[0].decode())
            msg_list.insert("end", str(o) + "\n")
            msg_list.itemconfigure("end", fg="blue")

        j = k.communicate()[1].decode()
        if j:
            print("error", j)
            messagebox.showinfo("process output", k.communicate()[1].decode())
            msg_list.insert("end", str(j)+"\n")
            msg_list.itemconfigure("end", fg="red")

        lis.clear()
    msg = None

    def send(event=None):
        global lis
        global msg
        nonlocal my_msg
        nonlocal entry_field
        msg = entry_field.get()
        print(msg, my_msg)
        my_msg.set("")
        if msg:
            lis.append(msg)
            print(lis)
            recieve()
        else:
            print("invalid input")

    def recieve():
        global msg
        nonlocal msg_list
        global lis
        if msg:
            msg_list.insert("end", str(msg))

    entry_field = tk.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tk.Button(top, text="Send", command=send)
    send_button.pack()
    run_button = tk.Button(top, text="Run", command=runcode)
    run_button.pack(side=tk.LEFT)
    top.mainloop()
def photocode():
    global text
    t = str(text.get(0.0, END)).rstrip()
    print(t)
    text.delete(0.0, END)

    value = cv2.imread(t)
    value = cv2.resize(value, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)
    value = cv2.cvtColor(value, cv2.COLOR_BGR2GRAY)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # value = cv2.filter2D(value, -1, kernel)
    img = Image.fromarray(value)
    enchancer = ImageEnhance.Sharpness(img)
    enchancer.enhance(15)
    enchancer = ImageEnhance.Color(img)
    enchancer.enhance(0)
    enchancer = ImageEnhance.Contrast(img)
    enchancer.enhance(4)
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
    # text=pytesseract.image_to_boxes(value)
    try:
        te = pytesseract.image_to_string(value)
        print("found", te)
    except:
        te="not found"
        print("not found")
    text.insert(END,"code"+"\n"+str(te) )


root=Tk()
root.title('my python text editor')
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)
text=Text(root,width=400,height=400)
text.pack()
menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='Open',command=openfile)
filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='Save As..',command=saveas)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=root.quit)
filemenu.add_command(label='JAVA',command=javaprogram)
filemenu.add_command(label='PYTHON',command=pythonprogram)
filemenu.add_command(label='C++',command=cprogram)
filemenu.add_command(label='HTML',command=txtml)
filemenu.add_command(label='photocode',command=photocode)
menubar.add_cascade(label="file",menu="menubar")
root.config(menu=filemenu)

root.mainloop()

