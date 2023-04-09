import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import Texthide
def main1():
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('800x650')
    root.configure(background='#001533')
    root.title('Encryptor')

    # function for Text Encryption
    def btnTxtEncry():
        text = multext.get("1.0", 'end-1c')
        text = Texthide.Texthide(text)
        multext2.insert(tk.END, text)


    # Name of the Option selected
    Label(root, text='Data Hiding in Text',fg="#F01154", bg='#001533', font=('fixedsys', 28, 'normal')).place(x=220, y=30)

    # Enter the text prompt
    Label(root, text='Enter Cover Text',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=51, y=200)

    # textbox for the input
    #tInput = Entry(root, font="Calibri 16")
    #tInput.place(x=240, y=202)


    # Text Widget
    #multext = tk.Text(root, width=27, height=4)
    #multext.place(x=240, y=202)
    multext = tk.Text(root, height=6, width=40)
    scroll = tk.Scrollbar(root)
    multext.configure(yscrollcommand=scroll.set)
    multext.place(x=240, y=202)

    scroll.config(command=multext.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # prompt for the showing encrypted text
    Label(root, text='Encrypted Text',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=52, y=380)

    # Output textbox
    #tOutput = Entry(root, font="Calibri 16")
    #tOutput.place(x=240, y=450)

    # Button for sending/saving the data
    Button(root, text='Encrypt it',
           fg="#001533",
           activeforeground='#04f8f8',
           activebackground='#001533',
           borderwidth=0,
           bg='#04f8f8',
           font=('verdana', 16, 'normal'),
           command=btnTxtEncry).place(
        x=240, y=320)

    # Text Widget
    # multext = tk.Text(root, width=27, height=4)
    # multext.place(x=240, y=202)
    multext2 = tk.Text(root, height=6, width=40)
    scroll = tk.Scrollbar(root)
    multext2.configure(yscrollcommand=scroll.set)
    multext2.place(x=240, y=380)

    scroll.config(command=multext2.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # exit button
    exit_button = Button(root, text="<<", fg="#001533",
                         activeforeground='#04f8f8',
                         activebackground='#001533',
                         borderwidth=0,
                         bg='#04f8f8', font=('verdana', 16, 'normal'),
                         command=root.destroy)
    exit_button.place(x=680, y=30)

    root.mainloop()
