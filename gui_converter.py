import tkinter as tk
from tkinter import ttk
from currency_exchange import Currency

def convert_currency():
    try:
        # get the input amount and selected currencies
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        # create a Currency object and perform conversion
        currency = Currency(amount, from_currency)
        currency.changeTo(to_currency)

        # display the converted amount
        result_label.config(text=f"Converted Amount: {currency}")
    except ValueError as e:
        result_label.config(text=f"Error: {str(e)}")

# create the main window
root = tk.Tk()
root.title("Currency Converter")

# create a frame for the conversion inputs
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# amount input
ttk.Label(frame, text="Amount:").grid(row=0, column=0, sticky=tk.W)
amount_entry = ttk.Entry(frame, width=20)
amount_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

# from currency dropdown
ttk.Label(frame, text="From Currency:").grid(row=1, column=0, sticky=tk.W)
from_currency_var = tk.StringVar()
from_currency_dropdown = ttk.Combobox(frame, textvariable=from_currency_var)
from_currency_dropdown['values'] = list(Currency.currencies.keys())
from_currency_dropdown.grid(row=1, column=1, sticky=(tk.W, tk.E))

# to currency dropdown
ttk.Label(frame, text="To Currency:").grid(row=2, column=0, sticky=tk.W)
to_currency_var = tk.StringVar()
to_currency_dropdown = ttk.Combobox(frame, textvariable=to_currency_var)
to_currency_dropdown['values'] = list(Currency.currencies.keys())
to_currency_dropdown.grid(row=2, column=1, sticky=(tk.W, tk.E))

# convert button
convert_button = ttk.Button(frame, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# result label
result_label = ttk.Label(frame, text="Converted Amount: ")
result_label.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

# set default values for dropdowns
from_currency_var.set("USD")
to_currency_var.set("EUR")

# start the GUI event loop
root.mainloop()