import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import Texthide
import Decryption

def main1():
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('800x650')
    root.configure(background='#001533')
    root.title('Encryptor')

    # function for Text Encryption
    def btnTxtDecry():
        text = multext.get("1.0",'end-1c')
        text = Texthide.Text_recover(text)
        text = Decryption.main(text)
        tOutput.insert(0, text)

    # Name of the Program
    #Label(root, text='Morse Code Encryptor', bg='#436EEE', font=('verdana', 18, 'bold')).place(x=239, y=24)

    # gratitude
    #Label(root, text='Thanks for using the Machine', bg='#436EEE', font=('helvetica', 16, 'bold')).place(x=231,y=67)

    # Name of the Option selected
    Label(root, text='Data Extraction from Text',fg="#F01154", bg='#001533', font=('fixedsys', 28, 'normal')).place(x=140, y=30)

    # Enter the text prompt
    Label(root, text='Enter your Encrypted Text',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=51, y=200)

    # textbox for the input
    # tInput = Entry(root, font="Calibri 16")
    # tInput.place(x=240, y=202)

    # Text Widget
    # multext = tk.Text(root, width=27, height=4)
    # multext.place(x=240, y=202)
    multext = tk.Text(root, height=6, width=40)
    scroll = tk.Scrollbar(root)
    multext.configure(yscrollcommand=scroll.set)
    multext.place(x=340, y=202)

    scroll.config(command=multext.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # prompt for the showing encrypted text
    Label(root, text='Extracted Message',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=52, y=390)

    # Output textbox
    tOutput = Entry(root, font="Calibri 16")
    tOutput.place(x=340, y=390)

    # Button for sending/saving the data
    Button(root, text='Decrypt it',
           fg="#001533",
           activeforeground='#04f8f8',
           activebackground='#001533',
           borderwidth=0,
           bg='#04f8f8',
           font=('verdana', 16, 'normal'),
           command=btnTxtDecry).place(
        x=340, y=320)

    # Text Widget
    # multext = tk.Text(root, width=27, height=4)
    # multext.place(x=240, y=202)
    #multext = tk.Text(root, height=6, width=40)
    #scroll = tk.Scrollbar(root)
    #multext.configure(yscrollcommand=scroll.set)
    #multext.place(x=340, y=390)

    #scroll.config(command=multext.yview)
    #scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # exit button
    exit_button = Button(root, text="<<",fg="#001533",
                         activeforeground='#04f8f8',
                         activebackground='#001533',
                         borderwidth=0,
                         bg='#04f8f8', font=('verdana', 16, 'normal'),
                         command=root.destroy)
    exit_button.place(x=680,y=30)

    root.mainloop()
