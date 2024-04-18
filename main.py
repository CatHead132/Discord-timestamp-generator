import tkinter as tk
from datetime import datetime
from discord_timestamps import format_timestamp, TimestampType
import clipboard


def get_future_timestamp(current_timestamp, offset_type, offset_value):
  if offset_type.lower() not in ("m", "h"):
    raise ValueError("Invalid offset type. Please enter 'm' for minutes or 'h' for hours.")

  offset_in_seconds = offset_value * (60 if offset_type.lower() == "m" else 3600)
  future_timestamp = current_timestamp + offset_in_seconds
  return future_timestamp


def calculate_timestamp():
  try:
    offset_type = offset_entry.get().lower()
    offset_value = int(offset_value_entry.get())
    if offset_value < 0:
      result_label.config(text="Offset value must be positive.")
      return

    current_timestamp = int(datetime.now().timestamp())
    future_timestamp = get_future_timestamp(current_timestamp, offset_type, offset_value)
    formatted_timestamp = format_timestamp(future_timestamp, TimestampType.RELATIVE)
    result_label.config(text=f"Discord Timestamp: {formatted_timestamp}")

    clipboard.copy(formatted_timestamp)

  except ValueError:
    result_label.config(text="Invalid input. Please try again.")


root = tk.Tk()
root.title("Discord Timestamp Generator")

offset_type_label = tk.Label(root, text="Offset Type (m or h):")
offset_type_label.pack()

offset_entry = tk.Entry(root)
offset_entry.pack()

offset_value_label = tk.Label(root, text="Offset Value:")
offset_value_label.pack()

offset_value_entry = tk.Entry(root)
offset_value_entry.pack()

calculate_button = tk.Button(root, text="Copy Timestamp", command=calculate_timestamp)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
