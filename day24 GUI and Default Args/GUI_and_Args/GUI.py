import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")

def button_clicked():
    print("I got clicked")

button = tkinter.Button(text ="Click me", command = button_clicked)
button.pack()

window.mainloop()