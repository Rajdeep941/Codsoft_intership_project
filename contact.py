import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return self.contacts

    def search_contacts(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def update_contact(self, old_contact, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact == old_contact:
                self.contacts[i] = new_contact
                return True
        return False

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            return True
        return False

class ContactApp:
    def __init__(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.title("Contact Management System")

        # Apply a style theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Style configuration
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TEntry", padding=6, font=("Arial", 12))

        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.name_label = ttk.Label(self.main_frame, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = ttk.Label(self.main_frame, text="Phone")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.phone_entry = ttk.Entry(self.main_frame)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(self.main_frame, text="Email")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.email_entry = ttk.Entry(self.main_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = ttk.Label(self.main_frame, text="Address")
        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.address_entry = ttk.Entry(self.main_frame)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(self.main_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = ttk.Button(self.main_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_button = ttk.Button(self.main_frame, text="Search Contacts", command=self.search_contacts)
        self.search_button.grid(row=5, column=0, padx=10, pady=10)

        self.update_button = ttk.Button(self.main_frame, text="Update Contact", command=self.update_contacts)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Contact", command=self.delete_contacts)
        self.delete_button.grid(row=6, column=0, padx=10, pady=10)

        self.exit_button = ttk.Button(self.main_frame, text="Exit", command=root.quit)
        self.exit_button.grid(row=6, column=1, padx=10, pady=10)

    def get_contact_details(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        return Contact(name, phone, email, address)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def add_contact(self):
        contact = self.get_contact_details()
        self.manager.add_contact(contact)
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added.")

    def view_contacts(self):
        contacts = self.manager.view_contacts()
        contact_list = "\n".join([str(contact) for contact in contacts])
        messagebox.showinfo("Contact List", contact_list if contact_list else "No contacts found.")

    def search_contacts(self):
        search_term = simpledialog.askstring("Search Contacts", "Enter name or phone number to search:")
        if search_term:
            results = self.manager.search_contacts(search_term)
            contact_list = "\n".join([str(contact) for contact in results])
            messagebox.showinfo("Search Results", contact_list if contact_list else "No contacts found.")

    def update_contacts(self):
        search_term = simpledialog.askstring("Update Contacts", "Enter name or phone number to search:")
        if search_term:
            results = self.manager.search_contacts(search_term)
            if results:
                for i, contact in enumerate(results):
                    messagebox.showinfo(f"Contact {i+1}", str(contact))
                index = int(simpledialog.askstring("Update Contact", "Choose a contact to update (number): ")) - 1
                old_contact = results[index]
                messagebox.showinfo("Enter new details", "Please enter new details in the main form and click 'Add Contact'")
                new_contact = self.get_contact_details()
                if self.manager.update_contact(old_contact, new_contact):
                    messagebox.showinfo("Success", "Contact updated.")
                else:
                    messagebox.showerror("Error", "Failed to update contact.")
            else:
                messagebox.showinfo("No contacts found", "No contacts found matching the search term.")

    def delete_contacts(self):
        search_term = simpledialog.askstring("Delete Contacts", "Enter name or phone number to search:")
        if search_term:
            results = self.manager.search_contacts(search_term)
            if results:
                for i, contact in enumerate(results):
                    messagebox.showinfo(f"Contact {i+1}", str(contact))
                index = int(simpledialog.askstring("Delete Contact", "Choose a contact to delete (number): ")) - 1
                contact = results[index]
                if self.manager.delete_contact(contact):
                    messagebox.showinfo("Success", "Contact deleted.")
                else:
                    messagebox.showerror("Error", "Failed to delete contact.")
            else:
                messagebox.showinfo("No contacts found", "No contacts found matching the search term.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()