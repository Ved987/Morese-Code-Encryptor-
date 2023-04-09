from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import LSB
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
        text = tInput.get()
        text = LSB.decode(text)
        text = Texthide.Text_recover(text)
        text = Decryption.main(text)
        tOutput.insert(0, text)

    # Name of the Option selected
    Label(root, text='Data Extraction from Image',fg="#F01154", bg='#001533', font=('fixedsys', 28, 'normal')).place(x=140, y=30)

    # Enter the text prompt
    Label(root, text='Enter Image name with extension',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=51, y=200)

    # textbox for the input
    tInput = Entry(root, font="Calibri 16")
    tInput.place(x=420, y=202)

    # prompt for the showing encrypted text
    Label(root, text='Extracted Data',fg="#04f8f8", bg='#001533', font=('verdana', 16, 'normal')).place(x=52, y=300)

    # Output textbox
    tOutput = Entry(root, font="Calibri 16")
    tOutput.place(x=420, y=300)

    # Button for sending/saving the data
    Button(root, text='Decrypt it',
           fg="#001533",
           activeforeground='#04f8f8',
           activebackground='#001533',
           borderwidth=0,
           bg='#04f8f8',
           font=('verdana', 16, 'normal'),
           command=btnTxtDecry).place(x=420, y=245)

    # exit button
    exit_button = Button(root, text="<<", fg="#001533",
                         activeforeground='#04f8f8',
                         activebackground='#001533',
                         borderwidth=0,
                         bg='#04f8f8', font=('verdana', 16, 'normal'),
                         command=root.destroy)
    exit_button.place(x=700, y=30)

    root.mainloop()
