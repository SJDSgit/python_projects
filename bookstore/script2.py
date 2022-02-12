from tkinter import *
 
window=Tk() # Create an empty Tkinter window
 
def from_kg():
    
    gram=float(e2_value.get())*1000 # Get user value from input box and multiply by 1000 to get kilograms
 
    pound=float(e2_value.get())*2.20462 # Get user value from input box and multiply by 2.20462 to get pounds
 
    ounce=float(e2_value.get())*35.274 # Get user value from input box and multiply by 35.274 to get ounces
 
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,gram)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)

e1=Label(window,text="Kg") # Create a Label widget with "Kg" as label
e1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window
 
e2_value=StringVar()  # Create a special StringVar object
e2=Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=1)

b1=Button(window,text="Convert",command=from_kg) # Create a button widget. The from_kg() function is called when the button is pushed
b1.grid(row=0,column=2) 
 
# Create three empty text boxes, t1, t2, and t3
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
 
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
 
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
 
window.mainloop() # This makes sure to keep the main window open