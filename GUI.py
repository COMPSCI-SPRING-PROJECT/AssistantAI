from tkinter import *


def func():
    i = Tk()
    Name = i.title("Avery")
    img = PhotoImage(file="bott.png")
    panel = Label(i, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    i.geometry('520x320')
    user = StringVar()
    user = LabelFrame(i, text='Avery', font=('Helvetica', 18, 'bold'))
    user.pack(fill='both', expand='yes')
    u = Message(user, textvariable=user, bg='black', fg='white')
    u.config(font=("railways", 15, 'bold'))
    u.pack(side='top', fill='both', expand='yes')
    clicks = Button(i, text="Speak", font=('Helvetica', 15,
                    'bold'), fg='red').pack(fill='x', expand='no')
    i.mainloop()


func()
