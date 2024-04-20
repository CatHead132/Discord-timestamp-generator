import customtkinter as ct
from datetime import datetime
import clipboard


def button_callback(entry):
    selected_unit = radiobutton_var.get()
    entry_text = entry.get()
    entry.delete(0, "end")

    if not entry_text:
        print("Please enter a value in the entry")
        return

    try:
        value = int(entry_text)
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return

    offset_in_seconds = 0
    if selected_unit == 0:
        offset_in_seconds = value * 86400
    elif selected_unit == 1:
        offset_in_seconds = value * 3600
    elif selected_unit == 2:
        offset_in_seconds = value * 60
    elif selected_unit == 3:
        offset_in_seconds = value
    else:
        print("Invalid unit selection")
        return

    current_timestamp = int(datetime.now().timestamp())
    future_timestamp = current_timestamp + offset_in_seconds

    timestamp = f"<t:{future_timestamp}:R>"

    clipboard.copy(timestamp)

    print(f"Generated Discord timestamp (relative) and copied to clipboard: {timestamp}")


# Create the main window
app = ct.CTk()
app.title("CatHead's Timestamp Generator")
app.geometry("300x200")
app.grid_columnconfigure((0), weight=1)

# Create variable to store radio button selection
radiobutton_var = ct.IntVar()

# Create radio buttons
radiobutton_1 = ct.CTkRadioButton(app, text="Days", variable=radiobutton_var, value=0)
radiobutton_1.grid(row=0, column=0, padx=20, pady=(0, 5), sticky="w")

radiobutton_2 = ct.CTkRadioButton(app, text="Hours", variable=radiobutton_var, value=1)
radiobutton_2.grid(row=1, column=0, padx=20, pady=(0, 5), sticky="w")

radiobutton_3 = ct.CTkRadioButton(app, text="Minutes", variable=radiobutton_var, value=2)
radiobutton_3.grid(row=2, column=0, padx=20, pady=(0, 5), sticky="w")

radiobutton_4 = ct.CTkRadioButton(app, text="Seconds", variable=radiobutton_var, value=3)
radiobutton_4.grid(row=3, column=0, padx=20, pady=(0, 5), sticky="w")

# Create the entry widget
entry = ct.CTkEntry(app, placeholder_text="Enter a value")
entry.grid(row=4, column=0, padx=15, pady=5, sticky="ew", columnspan=2)

# Generate button
button = ct.CTkButton(app, text="Generate", command=lambda: button_callback(entry))
button.grid(row=5, column=0, padx=20, pady=5, sticky="ew", columnspan=2)

# Start the GUI loop
app.mainloop()
