from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=250, height=150)
window.config(padx= 50, pady= 50)

#Labels
miles = Label(text="Miles", font=("Ubuntu", 12))
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Ubuntu", 12))
equal_to.grid(column=0, row=1)

result = Label()
result.grid(column=1, row=1)

kilometers = Label(text="km", font=("Ubuntu", 12))
kilometers.grid(column=2, row=1)

#button
def button_clicked():
    user_miles = int(input.get())
    answer = round(user_miles * 1.619, 3)
    result.config(text= answer)



button = Button(text="Calculate", command= button_clicked)
button.grid(column=1, row=2)


#entry -> it's an input

input = Entry(width=10)
input.grid(column=1, row=0)
















window.mainloop()