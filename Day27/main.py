import tkinter

window = tkinter.Tk()

window.title("Gui Program")
window.minsize(width=500,height=300)
#Padding
window.config(padx=100, pady=200)
#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.pack(side="left")
# my_label.pack(expand=True)
# my_label.pack()
# my_label.place(x=100,y=200)

my_label.grid(column=3, row=4)
my_label["text"] = "new text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Button
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me",command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
#i cant use pack with grid together


#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


#new button
button2 =tkinter.Button(text="cliiick",command=button_clicked)
button2.grid(column=2, row=0)
window.mainloop()




#example
# from tkinter import *
#
# root = Tk()

# ایجاد ویجت‌ها
# label1 = Label(root, text="نام:")
# entry1 = Entry(root)
# label2 = Label(root, text="نام خانوادگی:")
# entry2 = Entry(root)
#
# # قرار دادن با grid
# label1.grid(row=0, column=0)  # ردیف اول، ستون اول
# entry1.grid(row=0, column=1)  # ردیف اول، ستون دوم
# label2.grid(row=1, column=0)  # ردیف دوم، ستون اول
# entry2.grid(row=1, column=1)  # ردیف دوم، ستون دوم
#
# root.mainloop()