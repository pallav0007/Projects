from tkinter import *
from itertools import zip_longest
root=Tk()
root.title("Digital Electronics calculator")
root.geometry("535x390")
e = Entry(root, width=75, borderwidth=5)
e.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

def carryin():
    global carry
    carry=e.get()
    e.delete(0,END)
def notgate(num):
    if num is not 1:
        return 0
    return 1
def digisep(num):
    kis=list(int(i) for i in str(num))
    return kis
def dectobin(num,temp=None):
    if temp==None:
        temp=[]
    if num==0:
        kis=list(reversed(temp))
        kis = ''.join(map(str, kis))
        return int(kis)
    temp.append(num%2)
    return dectobin(num//2,temp)
def bintodec(num):
    s=list(int(i) for i in str(num))
    num=sum(int(c) * (2 ** i) for i, c in enumerate(s[::-1]))
    return num
def full_adder(a,b,c):
    lis=digisep(a)
    kis=digisep(b)
    his=[]
    for a,b in zip_longest(lis[::-1],kis[::-1]):
        his.append(xor(c,xor(a,b)))
        if a==b==1 or a==c==1 or b==c==1 or a==b==c==1:
            c=1
        else:
            c=0
        print(a,b,c)
        print(his)
    return ''.join(map(str, his[::-1])),c
def andg(num,tum):
    if num and tum is 1:
        return 1
    return 0
def org(num,tum):
    if num is not tum or ((num and tum ) is 1):
        return 1
    return 0
def xor(num,tum):
    if num is not tum:
        return 1
    return 0
def compliment(num):
    lis=list(int(i) for i in str(num))
    kis=list(0 if x==1 else 1 for x in lis )
    kis="".join(list(map(str,kis)))
    return kis

def buttonclick(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_or():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def buttonxor():
    first_number = e.get()
    global f_num
    global math
    math = "xor"
    f_num = int(first_number)
    e.delete(0, END)

def button_and():
    first_number = e.get()
    global f_num
    global math
    math = "andg"
    f_num = int(first_number)
    e.delete(0, END)
def button_adder():
    first_number = e.get()
    global f_num
    global math
    math = "adder"
    f_num = int(first_number)
    e.delete(0, END)

def button_dectobin():
    num = e.get()
    fnum=dectobin(int(num))
    e.delete(0, END)
    e.insert(0,fnum)
def buttonbd():
    num = e.get()
    fnum=bintodec(int(num))
    e.delete(0, END)
    e.insert(0,fnum)
def singleclear():
    e.delete(len(e.get()) - 1)
def clear():
    e.delete(0,END)
def compli():
    num=e.get()
    fnum=compliment(num)
    e.delete(0,END)
    e.insert(0,fnum)

def equate():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, org(f_num,int(second_number)))

    if math == "xor":
        e.insert(0, xor(f_num,int(second_number)))

    if math == "andg":
        e.insert(0, andg(f_num ,int(second_number)))

    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "adder":
        e.insert(0,full_adder(f_num,int(second_number),int(carry)))
        #print(carry)
def info():
    top=Toplevel()
    top.title("Calculator documentation")
    top.geometry("700x400")

    def how_adder():
        text = Text(top)
        text.insert(END, '''To carry out adder operation follow as under:-
    1.Click on carry i.e. no. to be given like 0 or 1 user want to give
    2.Click on carry
    3.Give your input 1 
    4.Click on adder and then give input 2
    ** Important: even if user add two number with different bits the program
    will automatically fill the remaining bit with 0 and give output ib longest
    bit i.e for 1111 adder 11 program will change it to 1111 adder 0011
            ''')
        text.grid(row=1,column=1,columnspan=30)
    def about():
            text=Text(top)
            text.insert(END,'''Hello from Pallav And Ruhaan hope you have pleasent experience with calculator 
    Our  Aim is to provide a basic device to help students and concerned person in basic electronic logic calculation
    1. The project is python based
    2. The only library used for project is tkinter for GUI
    3. It can perform 8 functions and have 12 functional keys
    4. The calculator has been made easy to use and efficient to meet most encountered and frequent operations''')
            text.grid(row=1,column=1,columnspan=30)
    def aboutkeys():
        text=Text(top)
        text.insert(END,'''
    1. Number keys - Print no. on screen and store for evaluation
    2. B - backspace
    3. C - clear 
    4. DB - convert decimal to binary
    5. BD - convert binary to decimal
    6. Carry - take no. on screen as carry
    7. Adder - use it as a operator like +,-,* or /
               use only after 1 input in given and then 
               given second input
    8. = - Equates whole operation for you
    9. XOR ,OR, AND -basic logic gates  
    10.COMP - gives 1's compliment of input given
    ''')
        text.grid(row=1,column=1,columnspan=30)

    button_how=Button(top,text="HOW TO USE ADDER",width=20,fg="white",bg="black",command=how_adder).grid(row=3,column=0,columnspan=6,sticky=W+E)
    buttonadder = Button(top, text="ABOUT PROGRAM",width=20,fg="white",bg="black",command=about).grid(row=1,column=0,columnspan=4,sticky=W+E)
    buttonkeys=Button(top,text="ABOUT KEYS",fg="white",bg="black",command=aboutkeys).grid(row=5,column=0,columnspan=6,sticky=W+E)
Button_1=Button(root,text=1, padx=41, pady=20,command=lambda:buttonclick(1)).grid(row=1,column=0)
Button_2=Button(root,text=2, padx=41, pady=20,command=lambda:buttonclick(2)).grid(row=1,column=1)
Button_3=Button(root,text=3, padx=41, pady=20,command=lambda:buttonclick(3)).grid(row=1,column=2)
Button_4=Button(root,text=4, padx=41, pady=20,command=lambda:buttonclick(4)).grid(row=2,column=0)
Button_5=Button(root,text=5, padx=41, pady=20,command=lambda:buttonclick(5)).grid(row=2,column=1)
Button_6=Button(root,text=6, padx=41, pady=20,command=lambda:buttonclick(6)).grid(row=2,column=2)
Button_7=Button(root,text=7, padx=41, pady=20,command=lambda:buttonclick(7)).grid(row=3,column=0)
Button_8=Button(root,text=8, padx=41, pady=20,command=lambda:buttonclick(8)).grid(row=3,column=1)
Button_9=Button(root,text=9, padx=41, pady=20,command=lambda:buttonclick(9)).grid(row=3,column=2)
Button_0=Button(root,text=0, padx=41, pady=20,command=lambda:buttonclick(0)).grid(row=4,column=1)
Button_org=Button(root,text="OR",width=5,fg="white",bg="blue", padx=40, pady=20,command=lambda:button_or()).grid(row=1,column=4)
Button_xor=Button(root,text="XOR",width=5,fg="white",bg="blue",  padx=40, pady=20,command=lambda:buttonxor()).grid(row=2,column=4)
Button_addg=Button(root,text="AND",width=5,fg="white",bg="blue",  padx=40, pady=20,command=lambda:button_and()).grid(row=3,column=4)
Button_dectobin=Button(root,text="DB",width=5,fg="white",bg="blue", padx=40, pady=20,command=lambda:button_dectobin()).grid(row=4,column=4)
Button_clear=Button(root,text="C", padx=40, pady=20,fg="white",bg="red",command=lambda:clear()).grid(row=4,column=2)
Button_equal=Button(root,text="=",width=40, padx=47, pady=20,fg="white",bg="purple",command=lambda:equate()).grid(row=5,column=0,columnspan=7,sticky=E+W)
Button_singleclear=Button(root,text="B", padx=40, pady=20,fg="white",bg="red",command=lambda:singleclear()).grid(row=4,column=0)
Button_bd=Button(root,text="BD",width=5,fg="white",bg="blue", padx=39, pady=20,command=lambda:buttonbd()).grid(row=1,column=5)
Button_carry=Button(root,text="CARRY",width=5,fg="white",bg="blue", padx=39, pady=20,command=lambda:carryin()).grid(row=2,column=5)
Button_adder=Button(root,text="ADDER",width=5,fg="white",bg="blue", padx=39, pady=20,command=lambda:button_adder()).grid(row=3,column=5)
Button_info=Button(root,text="INFO",width=5,fg="white",bg="green", padx=39, pady=20,command=lambda:info()).grid(row=4,column=5)
Button_comp=Button(root,text="COMP",width=5,fg="white",bg="black", padx=39, pady=20,command=lambda:compli()).grid(row=5,column=5)
root.mainloop()