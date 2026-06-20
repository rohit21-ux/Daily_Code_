from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys




def do_compute():
    # Prices for the stationary
    notebook = 40.00   # Price of notebook
    pen      = 10.00   # Price of pen
    pencil   = 5.00    # Price of pencil
    eraser   = 8.00    # Price of eraser
    

    qty1 = int(f1_str_var.get() or 0)
    qty2 = int(f2_str_var.get() or 0)
    qty3 = int(f3_str_var.get() or 0)
    qty4 = int(f4_str_var.get() or 0)

    if qty1 == 0 and qty2 == 0 and qty3 ==0 and qty4 == 0:
        messagebox.showwarning("No order", "Please!,Place order first... ")
        
        return

    print(qty1,qty2,qty3,qty4)

    # Calculate total bill
    total = (qty1 * notebook) + (qty2 * pen) + (qty3 * pencil) + (qty4 * eraser)
    print(total)
    


    # Display the total bill
    result.set(f'Total Bill: ₹{total:.2f}')
    

def do_clear():
    empty_str = ''
    f1_str_var.set(empty_str)
    f2_str_var.set(empty_str)
    f3_str_var.set(empty_str)
    f4_str_var.set(empty_str)
    result.set(empty_str)
    

def do_exit():
    sys.exit(0)

root_window = Tk()
root_window.title(" 🧾BILLING MENU DEMO")



input_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
input_frame.grid(row=0, column=0, padx=10, pady=10,sticky=(N,W,E,S))
input_frame.configure(relief='solid')

# Labels with rupee symbol
label_1 = ttk.Label(input_frame)
label_1.configure(font=('Verdana', 8, 'bold'),text='Enter quantity of notebook (₹40):')
label_1.grid(row=0, column=0, sticky='w', padx=10, pady=10)

label_2 = ttk.Label(input_frame)
label_2.configure(font=('Verdana', 8, 'bold'),text='Enter quantity of pen (₹10):')
label_2.grid(row=1, column=0, sticky='w', padx=10, pady=10)

label_3 = ttk.Label(input_frame)
label_3.configure(font=('Verdana', 8, 'bold'),text='Enter quantity of pencil (₹5):')
label_3.grid(row=2, column=0, sticky='w', padx=10, pady=10)

label_4 = ttk.Label(input_frame)
label_4.configure(font=('Verdana', 8, 'bold'),text='Enter quantity of eraser (₹8):')
label_4.grid(row=3, column=0, sticky='w', padx=10, pady=10)



# Entry
f1_str_var = StringVar()
f1_entry = Entry(input_frame)
f1_entry.configure(font=('Consolas', 14, 'bold'),textvariable=f1_str_var, bg="#99ACFF")
f1_entry.grid(row=0, column=1, padx=10, pady=12)

f2_str_var = StringVar()
f2_entry = Entry(input_frame)
f2_entry.configure(font=('Consolas', 14, 'bold'),textvariable=f2_str_var, bg="#99ACFF")
f2_entry.grid(row=1, column=1, padx=10, pady=12)

f3_str_var = StringVar()
f3_entry = Entry(input_frame)
f3_entry.configure(font=('Consolas', 14, 'bold'),textvariable=f3_str_var, bg="#99ACFF")
f3_entry.grid(row=2, column=1, padx=10, pady=12)

f4_str_var = StringVar()
f4_entry = Entry(input_frame)
f4_entry.configure(font=('Consolas', 14, 'bold'),textvariable=f4_str_var, bg="#99ACFF")
f4_entry.grid(row=3, column=1, padx=10, pady=12)


button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='solid')
button_frame.grid(row=1, column=0,padx=10,pady=10,sticky=(N,W,E,S))
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Buttons
compute_button = Button(button_frame)
compute_button.configure(font=('Century Gothic', 11, 'bold'),text='💰Compute Bill', command=do_compute ,bg="#78E790")
compute_button.grid(row=0, column=0,sticky=(N,W,E,S))

clear_button= Button(button_frame)
clear_button.configure(font=('Century Gothic', 11, 'bold'), text='🧹Clear', command=do_clear, bg="#E8FF83")
clear_button.grid(row=0, column=1, sticky=(N,W,E,S))

exit_button = Button(button_frame)
exit_button.configure( font=('Century Gothic', 11, 'bold'),text='👋Exit', command=do_exit,bg="#E06565")
exit_button.grid(row=0, column=2, sticky=(N,W,E,S))

# output frame
output_frame = ttk.Frame(root_window,padding= "3 3 12 12",borderwidth=10 ,relief='solid' )
output_frame.grid(row = 2,column=0,padx=10,pady=10,sticky=(N,W,E,S))
output_frame.columnconfigure(0,weight=1)

# Result labels 
result = StringVar()
result_label_1 = Label(output_frame)
result_label_1.configure( font=('Georgia', 11, 'italic','bold'),textvariable=result, bg="#FF8FF9")
result_label_1.grid(row=0, column=0, padx=10, pady=10,sticky="ew")

label_6= ttk.Label(output_frame, anchor='center')
label_6.configure( font=('Georgia', 11, 'italic','bold'),text='Thanks for visiting, come again!!', background="#78E48A",foreground="blue" )
label_6.grid(row=1,column=0, padx=10, pady=5,sticky='ew')





root_window.mainloop()
