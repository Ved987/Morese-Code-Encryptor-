import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import LSB
import Texthide


def main1():
    root = Tk()

    def btnTxtEncry():
        text = MulCover.get("1.0", 'end-1c')
        text = Texthide.Texthide(text)
        img = int(ImgSelect.get())
        if img == 1:
            img = "car.png"
        elif img == 2:
            img = "panda.png"
        elif img == 3:
            img = "tulip.png"
        elif img == 4:
            img = "japan.png"
        else:
            ImgLocation.insert(0, "Invalid Choice")
            return
        n_img = ImgName.get()
        n_img = n_img + ".png"
        LSB.encode(text, img, n_img)
        ImgLocation.insert(tk.END, "C:\\Users\\Vedanshu\\PycharmProjects\\pythonProject\\Project.exb\\MainGUI\\dist\\" + n_img)

    # Name of the option selected
    Label(root, text='Data Hiding in Image', fg="#F01154", bg='#001533', font=('fixedsys', 28, 'normal')).place(x=200,
                                                                                                                y=30)

    # This is the section of code which creates the main window
    root.geometry('800x650')
    root.configure(background='#001533')
    root.title('Encryptor')

    # --------------------FOR IMAGE ADDING CODE NOT READY ALSO DON'T DELETE--------------
    # This is showing up in the main window for some reason
    # my_img=ImageTk.PhotoImage(Image.open("IMG (1).png"))
    # my_label=Label(image=my_img)
    # my_label.place(x=812,y=222)

    # --------------CODE NOT READY ALSO DON'T DELETE-----------------------

    # This is the section of code which creates the a label
    Label(root, text='1', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=118, y=325)

    # This is the section of code which creates the a label
    Label(root, text='2', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=280, y=325)

    # This is the section of code which creates the a label
    Label(root, text='3', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=435, y=325)

    # This is the section of code which creates the a label
    Label(root, text='4', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=595, y=325)

    # Creating label for the image names
    # 1
    Label(root, text='car.png', fg="#04f8f8", bg='#001533', font=('verdana', 12, 'normal')).place(x=90, y=300)
    # 2
    Label(root, text='panda.png', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=250, y=300)
    # 3
    Label(root, text='tulip.png', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=410, y=300)
    # 4
    Label(root, text='japan.png', fg="#04f8f8", bg='#001533', font=('arial', 12, 'normal')).place(x=570, y=300)

    # Label for Select an Image(1,2,3,4)
    Label(root, text='Select an Image(1,2,3,4)', fg="#04f8f8", bg='#001533', font=('verdana', 12, 'normal')).place(x=50,
                                                                                                                   y=388)

    # Entry for Image Selection
    ImgSelect = Entry(root, width=20)
    ImgSelect.place(x=279, y=387)

    # Label for Cover Text
    Label(root, text='Enter the Cover Text', fg="#04f8f8", bg='#001533', font=('verdana', 12, 'normal')).place(x=45,
                                                                                                               y=154)

    # Entry for Cover Text
    # CoverText = Entry(root, width=50)
    # CoverText.place(x=229, y=153)

    # Multiline cover text entry point
    MulCover = tk.Text(root, height=5, width=40)
    scroll = tk.Scrollbar(root)
    MulCover.configure(yscrollcommand=scroll.set)
    MulCover.place(x=229, y=153)

    scroll.config(command=MulCover.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # This is the section of code which creates the a label
    Label(root, text='Type the new image name', fg="#04f8f8",
          activeforeground='#04f8f8',
          activebackground='#001533',
          borderwidth=0,
          bg='#001533', font=('verdana', 12, 'normal')).place(x=52, y=434)

    # This is the section of code which creates a text input box
    ImgName = Entry(root)
    ImgName.place(x=279, y=436)

    # This is the section of code which creates the a label
    Label(root, text='.png', fg="#04f8f8", bg='#001533', font=('verdana', 12, 'normal')).place(x=400, y=436)

    # This is the section of code which creates the a label
    Label(root, text='Location of the new Image', fg="#04f8f8",
          activeforeground='#04f8f8',
          activebackground='#001533',
          borderwidth=0,
          bg='#001533', font=('verdana', 12, 'normal')).place(x=52, y=540)

    # This is the section of code which creates a text input box
    ImgLocation = tk.Text(root, height=5, width=40)
    scroll = tk.Scrollbar(root)
    ImgLocation.configure(yscrollcommand=scroll.set)
    ImgLocation.place(x=278, y=540)

    scroll.config(command=MulCover.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    #ImgLocation = Entry(root)
    #ImgLocation.place(x=278, y=540)

    Button(root, text='Encrypt it',
           fg="#001533",
           activeforeground='#04f8f8',
           activebackground='#001533',
           borderwidth=0,
           bg='#04f8f8',
           font=('verdana', 16, 'normal'),
           command=btnTxtEncry).place(x=278, y=480)

    # exit button
    exit_button = Button(root, text="<<", fg="#001533",
                         activeforeground='#04f8f8',
                         activebackground='#001533',
                         borderwidth=0,
                         bg='#04f8f8', font=('verdana', 16, 'normal'),
                         command=root.destroy)
    exit_button.place(x=680, y=30)

    root.mainloop()
