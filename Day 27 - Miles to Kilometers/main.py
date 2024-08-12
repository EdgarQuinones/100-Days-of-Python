from tkinter import Button, Label, Entry, Tk


def miles_to_km():
    new_calculation = int(text_entry.get()) * 1.6
    calculation.config(text=new_calculation)


window = Tk()
window.minsize(width=100, height=100)
window.title("Miles to Km Converter")

top_left_corner = Label(padx=50)
top_left_corner.grid(column=0, row=0)

text_entry = Entry(width=10)
text_entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km_transfer = Label(text="is equal to")
km_transfer.grid(column=0, row=1)

calculation = Label(text="0")
calculation.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
