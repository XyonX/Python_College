import tkinter as tk

# Creating the main window

window = tk.Tk()
window.geometry("300x600")
window.title("Hola")

label1 = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

#label1.pack()

# Creating a button
button1 = tk.Button(
    text="Press",
    width="25",
    height="5",
    fg="orange",
    bg="black"
)
##button1.pack()



email_label = tk.Label(text="Enter Your Email ID :")
#email_label.pack(side="left")

#Creating a entry
email_entry = tk.Entry(fg="black", bg="grey", width=50)
#email_entry.pack(side="right")




button1  = tk.Button(text="1",height="30",width="30",bg="grey").grid(row=0,column=1)
button2  = tk.Button(text="2",height="30",width="30",bg="grey").grid(row=0,column=2)
button3  = tk.Button(text="3",height="30",width="30",bg="grey").grid(row=0,column=3)

button4  = tk.Button(text="4",height="30",width="30",bg="grey").grid(row=1,column=1)
button5  = tk.Button(text="5",height="30",width="30",bg="grey").grid(row=1,column=2)
button6  = tk.Button(text="6",height="30",width="30",bg="grey").grid(row=1,column=3)

button7  = tk.Button(text="7",height="30",width="30",bg="grey").grid(row=2,column=1)
button8  = tk.Button(text="8",height="30",width="30",bg="grey").grid(row=2,column=2)
button9  = tk.Button(text="9",height="30",width="30",bg="grey").grid(row=2,column=3)

# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()
# button7.pack()
# button8.pack()
# button9.pack()


window.mainloop()

