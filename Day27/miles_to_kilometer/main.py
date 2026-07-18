from tkinter import *

def convert():
    answer_label.config(text=float(miles.get()) * 1.609)

window= Tk()
window.title("Mile to Kilometer converter")
window.minsize(100,100)

miles_label = Label(text="مایل", font=("Arial", 10))
kilometer_label = Label(text="کیلومتر", font=("Arial", 10))
is_equal_label = Label(text="برابر هست با ", font=("Arial", 10))
answer_label = Label(font=("Arial", 10))

miles_label.grid(column=0, row=0)
kilometer_label.grid(column=0, row=1)
is_equal_label.grid(row=1, column=2)
answer_label.grid(column=1, row=1)

miles = Entry(width=10)
miles.insert(0,"0")
miles.grid(row=0, column=1)


calculate_button = Button(text="محاسبه", width=10, command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()