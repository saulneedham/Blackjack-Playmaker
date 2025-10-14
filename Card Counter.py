import tkinter as tk
from tkinter import *

#--------------------------------------------------------------------------

def display(num):
    global count
    count+=num
    labelCount = tk.Label(root, text='    '*32)
    labelCount.config(font=('Helvetica',60))
    canvas1.create_window(225, 100, window=labelCount)
    labelCount = tk.Label(root, text=count)
    labelCount.config(font=('Helvetica',60))
    canvas1.create_window(225, 100, window=labelCount)

def minus():
    global count
    display(-1)

def add(): 
    global count
    display(1)

#--------------------------------------------------------------------------

root = tk.Tk()

root.title('BJ Counter')

canvas1 = tk.Canvas(root, width = 450, height = 260)
canvas1.pack()

count=0
display(0)

#--------------------------------------------------------------------------

button0 = tk.Button(text='-1', command=minus, width=12, height=4)
canvas1.create_window(112, 220, window=button0)

button0 = tk.Button(text='+1', command=add, width=12, height=4)
canvas1.create_window(337, 220, window=button0)

labelN = tk.Label(root, text='10,J,Q,K,A')
canvas1.create_window(112, 160, window=labelN)

labelP = tk.Label(root, text='2,3,4,5,6')
canvas1.create_window(337, 160, window=labelP)

#--------------------------------------------------------------------------

root.mainloop()