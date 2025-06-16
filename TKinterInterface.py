from tkinter import * 

# Creating a new window
window = Tk()

# Setting window title
window.title("My Example")

# Create a input
entry_text = Entry(window, width= 30)

# Pack function is a geometry manager 
entry_text.pack()

# Set the focus to the input
entry_text.focus_set()

# Set window size 
window.geometry('300x150')

# Create a button with a function
def click_button():
    print(entry_text.get())
btn = Button(window, text='Clique aqui', width=20, command=click_button)
btn.pack()

# Function to draw the window
window.mainloop()