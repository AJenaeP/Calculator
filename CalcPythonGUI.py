'''
Created on May 9, 2022

@author: ajenaepompey
'''

"""README.txt
This is a calculator program that I have created using Python/Pycharm/Tkinter

This calculator only performs simple calculations

Implemented: list, match, for

Thank you for viewing!

"""
import tkinter
from tkinter import *

# creating window
window = Tk()
window.title("Calculator")
window.geometry("393x410")
window.resizable(False, False)
window.configure(background="#d4d2d5")
# creating textField
textField = Entry(window, justify= RIGHT)
textField.place(x=6, y=2, width=380, height=79)
textField.configure(background="white", foreground="black", font=("Kohinoor Devanagari", 29, "normal"), bg= "#97CC04")


#funtion to display numbers in text field
def button_click(number):
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0, str(current) + str(number))


# creating number buttons
bttn0 = tkinter.Button(window, text="0", command=lambda: button_click(0))
bttn1 = Button(window, text="1", command=lambda: button_click(1))
bttn2 = Button(window, text="2", command=lambda: button_click(2))
bttn3 = Button(window, text="3", command=lambda: button_click(3))
bttn4 = Button(window, text="4", command=lambda: button_click(4))
bttn5 = Button(window, text="5", command=lambda: button_click(5))
bttn6 = Button(window, text="6", command=lambda: button_click(6))
bttn7 = Button(window, text="7", command=lambda: button_click(7))
bttn8 = Button(window, text="8", command=lambda: button_click(8))
bttn9 = Button(window, text="9", command=lambda: button_click(9))
# Creating a list of buttons
numBttn = [bttn0, bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9]
# placing buttons on window
bttn0.place(x=101, y=340, width=95, height=65)
bttn1.place(x=6, y=145, width=95, height=65)
bttn2.place(x=101, y=145, width=95, height=65)
bttn3.place(x=196, y=145, width=95, height=65)
bttn4.place(x=6, y=210, width=95, height=65)
bttn5.place(x=101, y=210, width=95, height=65)
bttn6.place(x=196, y=210, width=95, height=65)
bttn7.place(x=6, y=275, width=95, height=65)
bttn8.place(x=101, y=275, width=95, height=65)
bttn9.place(x=196, y=275, width=95, height=65)

for i in numBttn:
    i.configure(font=("Ayuthaya", 20, "normal"), highlightbackground= "#2D7DD2", fg= 'black', relief= RAISED)


def button_neg():
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0, -1 * float(current))
    return

def button_clear():
    textField.delete(0, END)
    return

def button_del():
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0,current[:-1])
    return

def button_mult():
    first = textField.get()
    textField.delete(0, END)
    global num1
    num1 = float(first)
    global operator
    operator = "*"
    return

def button_div():
    first = textField.get()
    textField.delete(0, END)
    global num1
    num1 = float(first)
    global operator
    operator = "/"
    return

def button_sub():
    first = textField.get()
    textField.delete(0, END)
    global num1
    num1 = float(first)
    global operator
    operator = "-"
    return

def button_add():
    first = textField.get()
    textField.delete(0, END)
    global num1
    num1 = float(first)
    global operator
    operator = "+"
    return

def button_dec():
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0, current + ".")
    return

def button_enter():
    second = textField.get()
    num2 = float(second)
    textField.delete(0, END)
    match operator:
        case "*":
            textField.insert(0, num1*num2)
        case "/":
            textField.insert(0, num1/num2)
        case "-":
            textField.insert(0, num1-num2)
        case "+":
            textField.insert(0, num1+num2)
    return

def button_perc():
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0, float(current)/100)
    return

# Creating function buttons
negBttn = Button(window, text="(+/-)", command=lambda: button_neg(), highlightbackground= "#F45D01")
clearBttn = Button(window, text="Clear", command=lambda: button_clear(), highlightbackground= "#F45D01")
delBttn = Button(window, text="Delete", command=lambda: button_del(), highlightbackground= "#F45D01")
multBttn = Button(window, text="*", command=lambda: button_mult(), highlightbackground= "#EEB902")
divBttn = Button(window, text="÷", command=lambda: button_div(), highlightbackground= "#EEB902")
subBttn = Button(window, text="-", command=lambda: button_sub(), highlightbackground= "#EEB902")
addBttn = Button(window, text="+", command=lambda: button_add(), highlightbackground= "#EEB902")
decBttn = Button(window, text=".", command=lambda: button_dec(), highlightbackground= "#2D7DD2")
enterBttn = Button(window, text="Enter", command=lambda: button_enter(), highlightbackground= "#EEB902")
percBttn = Button(window, text="%", command=lambda: button_perc(), highlightbackground= "#2D7DD2")
# Creating a list of function buttons
funcButtons = [negBttn, clearBttn, delBttn, multBttn, divBttn, subBttn, addBttn, decBttn, enterBttn, percBttn]
# Placing function buttons on window
negBttn.place(x=6, y=80, width=95, height=65)
clearBttn.place(x=101, y=80, width=95, height=65)
delBttn.place(x=196, y=80, width=95, height=65)
multBttn.place(x=291, y=145, width=95, height=65)
divBttn.place(x=291, y=80, width=95, height=65)
subBttn.place(x=291, y=210, width=95, height=65)
addBttn.place(x=291, y=275, width=95, height=65)
decBttn.place(x=6, y=340, width=95, height=65)
enterBttn.place(x=291, y=340, width=95, height=65)
percBttn.place(x=196, y=340, width=95, height=65)
for i in funcButtons:
    i.configure(font=("Ayuthaya", 20, "normal"), fg = 'black', relief= RAISED)

window.mainloop()
