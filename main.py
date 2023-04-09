import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

# this is the function called when the button is clicked
import TxtDecry
import TxtEncry
import HiddenInTxt
import ExtractFromText
import DataHideInImage
import DataExtractFromImage

# function for Initializing
def btnInitial():
    import Morse1
    import Morse2
    import Messages


# function for Text Encryption
def btnTxtEncry():
    TxtEncry.main1()


# Function for text decryption
def btnTxtDecry():
    TxtDecry.main1()


# Function for data hiding in text
def btnDataTxt():
    HiddenInTxt.main1()


# function for data extraction from text
def btnDataExt():
    ExtractFromText.main1()


# function for data hiding in image
def btnImgHide():
    DataHideInImage.main1()

def btnImgExtr():
    DataExtractFromImage.main1()

root = Tk()

# This is the section of code which creates the main window
root.geometry('800x650')
root.configure(background='#001533')
root.title('Encryptor')

# --------Fonts---------

mfont = font.Font(family="Fixedsys",
                  size="40",
                  weight="bold")

# Name of the Program
Label(root, text='Morse Code Encryptor', fg="#F01154", bg='#001533', font=mfont).place(x=85, y=24)

# gratitude
Label(root, text='Thanks for using the Machine', bg='#001533', fg="#04f8f8", font=('helvetica', 12, 'bold')).place(
    x=270, y=100)

# Intialzing button
Button(root, text='Initialize the Machine', fg="#000000",
       bg='#DB4D61',
       font=('verdana', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61", command=btnInitial).place(
    x=270, y=140)

# Menu label
Label(root, text='Process Menu', fg="#04f8f8", bg='#001533', font=('helvatica', 18, 'normal')).place(x=100, y=198)

#By TEAM 47 label
Label(root, text='By TEAM 47', fg="#04f8f8", bg='#001533', font=('FIXEDSYS', 14, 'normal')).place(x=600, y=90)

# Data encryption in text button
#Use it if Img Button is req btn = PhotoImage(file="./button_encryption-of-text.png") and paste it after bg -"image=btn,"

Button(root,text="1.Encryption of Text               ",
       fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61", command=btnTxtEncry).place(x=100, y=244)

# Data decryption in text button
Button(root, text='2.Decryption of Morse Code  ', fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61", command=btnTxtDecry).place(x=100, y=306)

# Data hiding in text button
Button(root, text='3.Data Hiding in Text             ', fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61", command=btnDataTxt).place(x=100, y=367)

# Data extraction from text button
Button(root, text='4.Data Extraction from Text   ',
       fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61", command=btnDataExt).place(
    x=100, y=431)

# Data hiding in image button
Button(root, text='5.Data Hiding in Image          ',
       fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61",
       command=btnImgHide).place(x=100, y=490)

# Data Extracting from image button
Button(root, text='6.Data Extracting from Image',
       fg="#000000",
       bg='#1AD5FF',
       font=('segoe ui', 16, 'normal'),
       borderwidth=0,
       activebackground="#DB4D61",
       command=btnImgExtr).place(x=100, y=550)

# exit button
exit_button = Button(root, text="EXIT", fg="#001533",
                     activeforeground='#04f8f8',
                     activebackground='#001533',
                     borderwidth=0,
                     bg='#04f8f8', font=('verdana', 16, 'normal'),
                     command=root.destroy)
exit_button.place(x=700, y=595)

#-------LOGO-------
frame = Frame(root, width=250, height=250,bd=0,bg="#001533")
frame.pack()
frame.place(x=470,y=240)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("1.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img,bd=0)
label.pack()


root.mainloop()
