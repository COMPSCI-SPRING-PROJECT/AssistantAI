from tkinter import *
def func():
    i = Tk()
    Name = i.title("Avery")
    greetings = Label(text="How are you",fg="white",bg="black")
    button = Button(text="Speak",width=35,height=8,bg="yellow",fg="blue")
    greetings.pack()
    button.pack()
    img = PhotoImage(file="bott.png")
    panel = Label(i, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    i.mainloop()
    
func()
