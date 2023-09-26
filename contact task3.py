import tkinter as tk
from tkinter import messagebox

# Define a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required.")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    search_results.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
            search_results.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        new_phone = new_phone_entry.get()
        new_email = new_email_entry.get()
        new_address = new_address_entry.get()
        contacts[index]["Phone"] = new_phone
        contacts[index]["Email"] = new_email
        contacts[index]["Address"] = new_address
        update_contact_list()

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        update_contact_list()

# Function to clear all input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Create and place labels and entry fields for contact details
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons for adding, updating, and deleting contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()

# Create a listbox to display contacts
contact_listbox = tk.Listbox(root)
contact_listbox.pack()

# Entry and button for searching contacts
search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

# Create a listbox to display search results
search_results = tk.Listbox(root)
search_results.pack()

# Entry fields for updating contact details
new_phone_label = tk.Label(root, text="New Phone:")
new_phone_label.pack()
new_phone_entry = tk.Entry(root)
new_phone_entry.pack()

new_email_label = tk.Label(root, text="New Email:")
new_email_label.pack()
new_email_entry = tk.Entry(root)
new_email_entry.pack()

new_address_label = tk.Label(root, text="New Address:")
new_address_label.pack()
new_address_entry = tk.Entry(root)
new_address_entry.pack()

# Start the main loop
root.mainloop()