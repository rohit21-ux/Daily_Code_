from tkinter import *
from tkinter import ttk
import sys




def do_compute():
    # Prices for the food items 
    samosa = 15.00    # Price of samosa
    tea    = 5.00    # Price of tea
    noodles = 20.00  # Price of noodles
    bottle = 20.00    # Price of bottle
    

    qty1 = int(f1_str_var.get())
    qty2 = int(f2_str_var.get())
    qty3 = int(f3_str_var.get())
    qty4 = int(f4_str_var.get())

    print(qty1,qty2,qty3,qty4)

    # Calculate total bill
    total = (qty1 * samosa) + (qty2 * tea) + (qty3 * noodles) + (qty4 * bottle)
    print(total)
    


    # result with rupee symbol
    result.set(f'Total Bill: ₹{total:.2f}')
    

def do_clear():
    f1_str_var.set('')
    f2_str_var.set('')
    f3_str_var.set('')
    f4_str_var.set('')
    result.set('')
    

def do_exit():
    sys.exit(0)

root_window = Tk()
root_window.title("BILLING MENU DEMO")
root_window.minsize(400, 300)
root_window.maxsize(800, 600)
root_window.configure(bg='grey')

# Labels with rupee symbol
label_1 = ttk.Label(root_window)
label_1.configure(text='Enter quantity of samosa (₹15):')
label_1.grid(row=0, column=0, sticky='w', padx=10, pady=5)

label_2 = ttk.Label(root_window)
label_2.configure(text='Enter quantity of tea (₹5):')
label_2.grid(row=1, column=0, sticky='w', padx=10, pady=5)

label_3 = ttk.Label(root_window)
label_3.configure(text='Enter quantity of noodles (₹20):')
label_3.grid(row=2, column=0, sticky='w', padx=10, pady=5)

label_4 = ttk.Label(root_window)
label_4.configure(text='Enter quantity of water bottle (₹20):')
label_4.grid(row=3, column=0, sticky='w', padx=10, pady=5)

# Result Labels
label_5 = ttk.Label(root_window)
label_5.configure(text='Total Bill:')
label_5.grid(row=6, column=1, sticky='w', padx=10, pady=5)


label_6= ttk.Label(root_window)
label_6.configure(text='Thanks for visiting, come again!!')
label_6.grid(row=7,column=1,sticky='w', padx=10, pady=5)

# Entry
f1_str_var = StringVar()
f1_entry = Entry(root_window)
f1_entry.configure(textvariable=f1_str_var, bg="#99ACFF")
f1_entry.grid(row=0, column=1, padx=10, pady=5)

f2_str_var = StringVar()
f2_entry = Entry(root_window)
f2_entry.configure(textvariable=f2_str_var, bg="#99ACFF")
f2_entry.grid(row=1, column=1, padx=10, pady=5)

f3_str_var = StringVar()
f3_entry = Entry(root_window)
f3_entry.configure(textvariable=f3_str_var, bg="#99ACFF")
f3_entry.grid(row=2, column=1, padx=10, pady=5)

f4_str_var = StringVar()
f4_entry = Entry(root_window)
f4_entry.configure(textvariable=f4_str_var, bg="#99ACFF")
f4_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
button_handle_1 = Button(root_window)
button_handle_1.configure(text='Compute Bill', command=do_compute, bg='yellow')
button_handle_1.grid(row=4, column=0, padx=25, pady=25)

button_handle_2= Button(root_window)
button_handle_2.configure( text='Clear', command=do_clear, bg='yellow')
button_handle_2.grid(row=4, column=1, padx=25, pady=25)

button_handle_3 = Button(root_window)
button_handle_3.configure(text='Exit', command=do_exit, bg='yellow')
button_handle_3.grid(row=4, column=2, padx=25, pady=25)

# Result labels 
result = StringVar()
result_label_1 = Label(root_window)
result_label_1.configure(textvariable=result, bg='lightgray')
result_label_1.grid(row=6, column=1, padx=10, pady=5)



root_window.mainloop()
