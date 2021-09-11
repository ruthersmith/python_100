import tkinter as tk


def mile_to_kilo():
    miles = mile_input.get()
    km = float(miles) * 1.609
    kilo_result_label.config(text=str(km))


window = tk.Tk()
window.title('miles to kilo converter')
window.config(padx=20, pady=20)

mile_input = tk.Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

isequal_label = tk.Label(text="is equal")
isequal_label.grid(column=0, row=1)

kilo_result_label = tk.Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = tk.Label(text="km")
kilo_label.grid(column=3, row=1)

calculate_button = tk.Button(text='calculate', command=mile_to_kilo)
calculate_button.grid(column=1, row=2)

window.mainloop()
