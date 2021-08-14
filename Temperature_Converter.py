 # Function used to convert temps 

def conversion(): 
    if (text.get() == "Fahrenheit" and  text2.get()=="Celsius"): 
        #(F − 32) × 5/9 = -17.78°C [FORMULA]
        a=number.get()   # Fetching the input given by user
        a -= 32
        b= a * (5/9)
        
        output_box.insert(tk.INSERT,b)
    elif (text.get() == text2.get()):
        messagebox.showerror("Error", "Cannot convert into same unit")
    else:   
        #(C × 9/5) + 32 = °F  [FORMULA]
        x=number.get()   # Fetching the input given by user
        y= x* 9/5
        y += 32
        output_box.insert(tk.INSERT,y)

# Function used to clear the input as well as ouput.

def clear():
    input_entrybox.delete(0,'end')
    output_box.delete('0.0',"end")
    
# Importing the required libraries
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox 
from tkinter import *

# GUI Code
root= tk.Tk()
root.resizable(False,False)
root.title("Temperature Converter")
root.configure(bg="#5B0E2D")

#Main Label
main_title=ttk.Label(root,text="Please Enter Temperature",font=('arial',13,'bold'),
foreground="#FFA781",background="#5B0E2D")
main_title.grid(column=0,row=1)

# Entry Box to get user input
number=tk.IntVar()
input_entrybox=ttk.Entry(root,width=40,textvariable=number)
input_entrybox.grid(column=0,row=2,pady=3,padx=2)
input_entrybox.focus()

# Label for 'from_unit'
from_label=ttk.Label(root,text="FROM :",font=('arial',13,'italic bold'),
foreground="#FFA781",background="#5B0E2D")
from_label.grid(column=7,row=1)

# Combobox used to select 'From_unit' from user
text=tk.StringVar()
from_type=ttk.Combobox(root,width=10,textvariable=text)
from_type.grid(column=7,row=2,padx=5)
from_type['values']=["Celsius","Fahrenheit"]

# Button for converting the temp to respective unit
convert_button=ttk.Button(root,text="Convert!",command=conversion)
convert_button.grid(column=1,row=3)

# Label for result 
result_label=ttk.Label(root,text="Result",font=('arial',13,'bold'),
foreground="#FFA781",background="#5B0E2D")
result_label.grid(column=0,row=5)

# This scrolled is text box of getting the output from program
output_box=st.ScrolledText(root,width=35,height=3,font=('arial',10))
output_box.grid(column=0,row=6,padx=5)

# Label for 'to_unit'
to_label=ttk.Label(root,text="TO :",font=('arial',13,'italic bold'),
foreground="#FFA781",background="#5B0E2D")
to_label.grid(column=7,row=5)

# This is combobox used to let user select the desired 'to_unit' for conversion
text2=tk.StringVar()
to_type=ttk.Combobox(root,width=10,textvariable=text2)
to_type['values']=["Celsius","Fahrenheit"]
to_type.grid(column=7,row=6,padx=5)

# It is a clear button used to clear input as well as ouput
clear_button=ttk.Button(root,text='Clear all',command=clear)
clear_button.grid(column=1,row=7,pady=5)

root.mainloop()

# END