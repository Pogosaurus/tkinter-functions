from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
import time

def step():
    for i in range(10):
        a.update_idletasks()
        p1['value'] += 10
        time.sleep(1)
        l2['text'] = p1['value'],'%'

def step2():
    for i in range(10):
        a.update_idletasks()
        p2['value'] += 10
        time.sleep(1)
        l3['text'] = p2['value'],'%'


a = Tk()
a.geometry("500x700")

LS1 = Label(a).grid(row =5, column =0)
LT1 = Label(a, text = '2. Label :').grid(row =6, column =0)
#Label
l1 = Label(a,text = "This is a Label").grid(row =7, column =0)

LS2 = Label(a).grid(row =8, column =0)
LT2 = Label(a, text = '3. Button :').grid(row =9, column =0)
#Button
b1 = Button(a,text = 'This is a Button', command = lambda : d.get()).grid(row =10, column =0)

LS3 = Label(a).grid(row =11, column =0)
LT3 = Label(a, text = '4. Entry :').grid(row =12, column =0)
#Entry
input1 = Entry(a).grid(row =13, column =0)

LS4 = Label(a).grid(row =14, column =0)
LT4 = Label(a, text = '5. Progressbar :').grid(row =15, column =0)
#Progressbar
p1 = Progressbar(a, length =110, orient =HORIZONTAL, mode = 'determinate')
p1['value'] = 0
p1.grid(row =16, column =10)
l2 = Label(a, text = '0')
l2.grid(row =16, column =20)
b2 = Button(a, text = 'Start Progressbar', command = step)
b2.grid(row =16, column =0)

p2 = Progressbar(a, length =110, orient =HORIZONTAL, mode = 'indeterminate')
p2['value'] = 0
p2.grid(row =17, column =10)
l3 = Label(a, text = '0')
l3.grid(row =17, column =20)
b3 = Button(a, text = 'Start Progressbar', command = step2)
b3.grid(row =17, column =0)

LS5 = Label(a).grid(row =18, column =0)
LT5 = Label(a, text = '6. Spinbox :').grid(row =19, column =0)
#Spinbox
s1 = Spinbox(a, values = ('Item 1','Item 2', 'Item 3', 'Item 4'))
s2 = Spinbox(a, from_ =1, to =10)
s1.grid(row =20, column=0)
s2.grid(row =21, column=0)

LS6 = Label(a).grid(row =22, column =0)
LT6 = Label(a, text = '7. Checkbox :').grid(row =23, column =0)
#Checkbok
c1 = Checkbutton(a, text = 'option 1', onvalue = 1).grid(row= 24, column =0)

LS7 = Label(a).grid(row =25, column =0)
LT7 = Label(a, text = '8. Radiobutton :').grid(row =26, column =0)
#Radiobutton
r1 = Radiobutton(a, text = 'option 1', value = 1).grid(row= 27, column =0)

LS8 = Label(a).grid(row =28, column =0)
LT8 = Label(a, text = '9. Dropdownbox :').grid(row =29, column =0)
#Dropdown Box
d = ttk.Combobox(a, width = 20)
d['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
d.grid(row =30, column =0)
d.current(0)

LS9 = Label(a).grid(row =31, column =0)
LT9 = Label(a, text = '10. Scale :').grid(row =32, column =0)
#Scale
d = Scale(a, from_ =1, to =100, orient =HORIZONTAL).grid(row =33, column = 0)

LT10 = Label(a, text = '1. Menubar :').grid(row =0, column =0)
#Menu
MenuBar1 = Menu(a)
SubMenu1 = Menu(MenuBar1)
MenuBar1.add_cascade(label = 'Option 1', menu = SubMenu1)
SubMenu1.add_command(label = '1', command = None)
SubMenu1.add_command(label = '2', command = None)
SubMenu1.add_command(label = '3', command = None)
SubMenu1.add_command(label = '4', command = None)
SubMenu1.add_separator()
SubMenu1.add_command(label = 'Exit', command = a.destroy)


SubMenu2 = Menu(MenuBar1)
MenuBar1.add_cascade(label = 'Option 2', menu = SubMenu2)
SubMenu2.add_command(label = 'A', command = None)
SubMenu2.add_command(label = 'B', command = None)
SubMenu2.add_command(label = 'C', command = None)
SubMenu2.add_command(label = 'D', command = None)
a.config(menu = MenuBar1)

a.mainloop()
