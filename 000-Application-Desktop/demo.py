# import tkinter as tk
# from tkinter import messagebox
# import sqlite3

# def add_contact():
#     name = name_entry.get()
#     number = number_entry.get()
#     if name and number:
#         conn = sqlite3.connect("phonebook.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
#         conn.commit()
#         conn.close()
#         display_contacts()
#         name_entry.delete(0, tk.END)
#         number_entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Missing Information", "Please enter both name and number.")

# def delete_contact():
#     selected_index = contacts_list.curselection()
#     if selected_index:
#         conn = sqlite3.connect("phonebook.db")
#         cursor = conn.cursor()
#         selected_contact = contacts_list.get(selected_index)
#         name, number = selected_contact.split(": ")
#         cursor.execute("DELETE FROM contacts WHERE name = ? AND number = ?", (name, number))
#         conn.commit()
#         conn.close()
#         display_contacts()
#     else:
#         messagebox.showwarning("No Selection", "Please select a contact to delete.")

# def display_contacts():
#     contacts_list.delete(0, tk.END)
#     conn = sqlite3.connect("phonebook.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM contacts")
#     rows = cursor.fetchall()
#     for row in rows:
#         contacts_list.insert(tk.END, f"{row[0]}: {row[1]}")
#     conn.close()

# # Create the main window
# root = tk.Tk()
# root.title("Phone Book")
# root.geometry("800x600")

# # Create input fields for name and number
# name_label = tk.Label(root, text="Name:", font=("Helvetica", 14))
# name_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
# name_entry = tk.Entry(root, font=("Helvetica", 14))
# name_entry.grid(row=0, column=1, padx=10, pady=10)

# number_label = tk.Label(root, text="Number:", font=("Helvetica", 14))
# number_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
# number_entry = tk.Entry(root, font=("Helvetica", 14))
# number_entry.grid(row=1, column=1, padx=10, pady=10)

# # Create a Listbox to display contacts
# contacts_list = tk.Listbox(root, width=40, font=("Helvetica", 14))
# contacts_list.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# # Create buttons for adding and deleting contacts
# add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Helvetica", 14))
# add_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Helvetica", 14))
# delete_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# # Initialize the database and display existing contacts
# conn = sqlite3.connect("phonebook.db")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
#                   (name TEXT, number TEXT)''')
# conn.close()
# display_contacts()

# # Run the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3

def get_all_contacts():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    
    contacts_dict = {}
    for row in rows:
        contacts_dict[row[0]] = row[1]
    
    return contacts_dict

def handle_selection(event):
    selected_name = selected_contact.get()
    selected_number.set(contacts[selected_name])

# Create the main window
root = tk.Tk()
root.title("Phone Book")

# Get all contacts
contacts = get_all_contacts()

# Create a StringVar to hold the selected contact name and number
selected_contact = tk.StringVar()
selected_number = tk.StringVar()

# Create a Combobox to display the list of contacts
contact_combobox = ttk.Combobox(root, textvariable=selected_contact, values=list(contacts.keys()), state="readonly")
contact_combobox.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field to display the selected contact's number
number_entry = tk.Entry(root, textvariable=selected_number, state="readonly")
number_entry.grid(row=0, column=1, padx=10, pady=10)

# Bind an event to handle selection change
contact_combobox.bind("<<ComboboxSelected>>", handle_selection)

# Run the Tkinter event loop
root.mainloop()
