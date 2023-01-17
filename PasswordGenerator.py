from tkinter import *
import random

root = Tk()
root.title('Random Password Generator')


passwordNum = Label(root, text = "Select the number of password to be generated")
passwordLength = Label(root, text = "Select the length of password")

passwordNum.grid(column=1 , row=1)
passwordLength.grid(column=1, row=3)

spin1 = Spinbox(root, from_=2, to=20, width=5)
spin2 = Spinbox(root, from_=5, to=15, width=5)

spin1.grid(column=1, row=2)
spin2.grid(column=1, row=4)

chars = "abcdefghijklmnopqrstuvwxyz12394567890!@#$%^&*/?ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clicked():
    i = 0
    t.delete('1.0', END)
    while i < int(spin1.get()):
        passd = ""
        while len(passd) < int(spin2.get()):
            passd += chars[random.randint(0, len(chars)-1)]    
        t.insert(INSERT,f"Password {i + 1}: " + passd + "\n")
        i+=1        

def clear():
    t.delete('1.0', END)

btn = Button(root, text="Generate", command=clicked)
btn1 = Button(root, text="Clear", command=clear)
btn.grid(column=1,row=6)
btn1.grid(column=1,row=8)

t = Text(root, height=20, width=60)
t.grid(column=1, row=12)

root.mainloop()

