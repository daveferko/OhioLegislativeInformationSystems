import tkinter as tk
from tkinter import messagebox

# List to store previous entries
previous_entries = []

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    title = title_entry.get()
    hometown = hometown_entry.get()

    # Check if each field is empty and display specific error messages
    if not name:
        messagebox.showwarning("Input Error", "Name is required!")
    elif not title:
        messagebox.showwarning("Input Error", "Title is required!")
    else:
        # Add the entered data to the list of previous entries
        previous_entries.append((name, age, title, hometown))
        
        # Clear the fields after submission
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        hometown_entry.delete(0, tk.END)

        # Show confirmation page with the data and previous entries
        show_confirmation_page(name, age, title, hometown)

# Function to show confirmation page with entered data and previous entries
def show_confirmation_page(name, age, title, hometown):
    # Create a new window for the confirmation page
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmation Page")
    
    # Display the entered information
    tk.Label(confirmation_window, text="Confirmation Page", font=("Arial", 14)).pack(pady=10)
    tk.Label(confirmation_window, text=f"Name: {name}").pack()
    tk.Label(confirmation_window, text=f"Age: {age}").pack()
    tk.Label(confirmation_window, text=f"Title: {title}").pack()
    tk.Label(confirmation_window, text=f"Hometown: {hometown}").pack()
    
    # Display a table of previous entries
    tk.Label(confirmation_window, text="\nPrevious Entries:", font=("Arial", 12)).pack(pady=10)
    
    table_frame = tk.Frame(confirmation_window)
    table_frame.pack(pady=10)
    
    # Create table headers
    tk.Label(table_frame, text="Name", width=15, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(table_frame, text="Age", width=10, borderwidth=1, relief="solid").grid(row=0, column=1)
    tk.Label(table_frame, text="Title", width=15, borderwidth=1, relief="solid").grid(row=0, column=2)
    tk.Label(table_frame, text="Hometown", width=15, borderwidth=1, relief="solid").grid(row=0, column=3)
    
    # Populate the table with previous entries
    for i, entry in enumerate(previous_entries, start=1):
        tk.Label(table_frame, text=entry[0], width=15, borderwidth=1, relief="solid").grid(row=i, column=0)
        tk.Label(table_frame, text=entry[1], width=10, borderwidth=1, relief="solid").grid(row=i, column=1)
        tk.Label(table_frame, text=entry[2], width=15, borderwidth=1, relief="solid").grid(row=i, column=2)
        tk.Label(table_frame, text=entry[3], width=15, borderwidth=1, relief="solid").grid(row=i, column=3)

# Create the main window
root = tk.Tk()
root.title("Legislative Information Systems")

# Create and place labels and input fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Title").grid(row=2, column=0, padx=10, pady=10)
title_entry = tk.Entry(root)
title_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Hometown").grid(row=3, column=0, padx=10, pady=10)
hometown_entry = tk.Entry(root)
hometown_entry.grid(row=3, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start the application
root.mainloop()
