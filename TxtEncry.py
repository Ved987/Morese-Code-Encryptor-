from tkinter import *
import tkinter.font as font
import tkinter as tk
import Encrypt1
import Encrypt2
import dispenc
def main1():
    root = Tk()
    # This is the section of code which creates the main window
    root.geometry('800x650')
    root.configure(background='#001533')
    root.title('Encryptor')

    # function for Text Encryption
    def btnTxtEncry():
        key = int(tKey.get())
        text = tInput.get()
        Encrypt1.main(text,key)
        Encrypt2.main()
        multext.insert(tk.END, dispenc.main())

    # Name of the Option selected
    Label(root, text='Text Encryption',
          fg="#F01154",
          bg='#001533',
          font=('fixedsys', 28, 'normal')).place(x=240, y=30)

    # Enter the text prompt
    Label(root, text='Enter your Secret Message',
          fg="#04f8f8",
          bg='#001533',
          font=('verdana', 16, 'normal')).place(x=51, y=200)

    # textbox for the input
    tInput = Entry(root, font="Calibri 16", )
    tInput.place(x=340, y=202)

    # Enter the Key prompt
    Label(root, text='Enter your Key',
          bg='#001533',
          fg="#04f8f8",
          font=('verdana', 16, 'normal')).place(x=51, y=240)

    # textbox for the Key
    tKey = Entry(root, font="Calibri 16")
    tKey.place(x=340, y=240)

    # prompt for the showing encrypted text
    Label(root, text='Encrypted Morse Code',
          bg='#001533',
          fg="#04f8f8",
          font=('verdana', 16, 'normal')).place(x=52, y=375)

    # Output textbox
    #tOutput = Entry(root, font="Calibri 16")
    #tOutput.place(x=340, y=375)
    # OPlab=Label(root, bg='#436EEE', font=('verdana', 16, 'normal')).place(x=72, y=375)

    # text widget
    multext = tk.Text(root, height=6, width=40)
    scroll = tk.Scrollbar(root)
    multext.configure(yscrollcommand=scroll.set)
    multext.place(x=340, y=375)

    scroll.config(command=multext.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Button for sending/saving the data
    Button(root, text='Encrypt it',
           fg="#001533",
           activeforeground='#04f8f8',
           activebackground='#001533',
           borderwidth=0,
           bg='#04f8f8',
           font=('verdana', 16, 'normal'),
           command=btnTxtEncry).place(x=340, y=285)
    # exit button
    exit_button = Button(root, text="<<", fg="#001533",
                         activeforeground='#04f8f8',
                         activebackground='#001533',
                         borderwidth=0,
                         bg='#04f8f8', font=('verdana', 16, 'normal'),
                         command=root.destroy)
    exit_button.place(x=700, y=25)

    root.mainloop()
