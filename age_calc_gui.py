from tkinter import *
from datetime import date

# Initialize the main window
root = Tk()
root.geometry('300x300')  # Adjust window size as needed
root.resizable(False, False)  # Disable resizing
root.title('Age Calculator')

# Function to calculate and display age
def calculate_age():
    global statement
    statement.destroy()  # Remove previous output

    try:
        # Get user input and convert to integers
        name = name_entry.get().strip()  # Get name with leading/trailing spaces removed
        birth_year = int(year_entry.get())
        birth_month = int(month_entry.get())
        birth_day = int(day_entry.get())

        # Validate user input (optional)
        if birth_year < 1900 or birth_year > 2024:
            raise ValueError("Invalid year. Please enter a year between 1900 and 2024.")
        if birth_month < 1 or birth_month > 12:
            raise ValueError("Invalid month. Please enter a month between 1 and 12.")
        if birth_day < 1 or birth_day > 31:
            raise ValueError("Invalid day. Please enter a day between 1 and 31.")

        # Calculate age
        today = date.today()
        age = today.year - birth_year
        if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
            age -= 1

        # Display output
        statement = Label(root, text=f"{name}'s age is {age}.")
        statement.grid(row=6, column=1, pady=15)

    except ValueError as e:
        # Handle invalid input gracefully
        statement = Label(root, text=str(e))
        statement.grid(row=6, column=1, pady=15)

# Create labels and entry fields
name_label = Label(root, text="Name: ")
name_label.grid(row=1, column=0, padx=5, pady=5)

name_value = StringVar()
name_entry = Entry(root, textvariable=name_value)
name_entry.grid(row=1, column=1, padx=5, pady=5)

year_label = Label(root, text="Year: ")
year_label.grid(row=2, column=0, padx=5, pady=5)

year_value = StringVar()
year_entry = Entry(root, textvariable=year_value)
year_entry.grid(row=2, column=1, padx=5, pady=5)

month_label = Label(root, text="Month: ")
month_label.grid(row=3, column=0, padx=5, pady=5)

month_value = StringVar()
month_entry = Entry(root, textvariable=month_value)
month_entry.grid(row=3, column=1, padx=5, pady=5)

day_label = Label(root, text="Day: ")
day_label.grid(row=4, column=0, padx=5, pady=5)

day_value = StringVar()
day_entry = Entry(root, textvariable=day_value)
day_entry.grid(row=4, column=1, padx=5, pady=5)

# Create button for calculating age
calculate_button = Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=5, column=1, padx=5, pady=5)

# Display initial output (optional)
statement = Label(root, text="Enter your details to calculate your age.")
statement.grid(row=6, column=1, pady=15)

# Run the main event loop
root.mainloop()