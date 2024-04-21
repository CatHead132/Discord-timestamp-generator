import customtkinter as ct
from datetime import datetime
import clipboard
import random


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
    else:
        print("Invalid unit selection")
        return

    current_timestamp = int(datetime.now().timestamp())
    future_timestamp = current_timestamp + offset_in_seconds

    timestamp = f"<t:{future_timestamp}:R>"

    clipboard.copy(timestamp)

    print(f"Generated Discord timestamp (relative) and copied to clipboard: {timestamp}")


def rng_event():
  max = entry2.get()
  min = entry3.get()
  entry2.delete(0, "end")
  entry3.delete(0, "end")

  if min == "":
    min = 0

  random_number = random.randint(int(min), int(max))
  label.configure(text=random_number)

  return


# Create the main window
app = ct.CTk()
app.title("CatHead's Timestamp Generator")
app.geometry("400x225")
app.grid_columnconfigure((0), weight=1)

radiobutton_var = ct.IntVar()

app.frame = ct.CTkFrame(app)
app.frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

app.title1 = ct.CTkLabel(app.frame, text="TimeStamp", fg_color="gray30", corner_radius=6)
app.title1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

radiobutton_1 = ct.CTkRadioButton(app.frame, text="Days", variable=radiobutton_var, value=0)

radiobutton_1.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")

radiobutton_2 = ct.CTkRadioButton(app.frame, text="Hours", variable=radiobutton_var, value=1)
radiobutton_2.grid(row=2, column=0, padx=20, pady=(0, 5), sticky="w")

radiobutton_3 = ct.CTkRadioButton(app.frame, text="Minutes", variable=radiobutton_var, value=2)
radiobutton_3.grid(row=3, column=0, padx=20, pady=(0, 5), sticky="w")


entry = ct.CTkEntry(app.frame, placeholder_text="Enter a value")
entry.grid(row=4, column=0, padx=15, pady=5, sticky="ew", columnspan=2)

button = ct.CTkButton(app.frame, text="Copy", command=lambda: button_callback(entry))
button.grid(row=5, column=0, padx=20, pady=5, sticky="ew", columnspan=2)

app.frame2 = ct.CTkFrame(app)
app.frame2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsw")
app.title2 = ct.CTkLabel(app.frame2, text="RNG", fg_color="gray30", corner_radius=6)
app.title2.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
entry2 = ct.CTkEntry(app.frame2, placeholder_text="Max")
entry2.grid(row=1, column=0, padx=15, pady=5, sticky="ew", columnspan=2)
entry3 = ct.CTkEntry(app.frame2, placeholder_text="Min")
entry3.grid(row=2, column=0, padx=15, pady=5, sticky="ew", columnspan=2)
button2 = ct.CTkButton(app.frame2, text="Generate", command=rng_event)
button2.grid(row=3, column=0, padx=15, pady=5, sticky="ew", columnspan=2)
label = ct.CTkLabel(app.frame2, text="Result", fg_color="transparent")
label.grid(row=4, column=0, padx=15, pady=5, sticky="ew", columnspan=2)


app.mainloop()
