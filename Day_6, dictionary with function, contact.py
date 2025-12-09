# Simple Contact Book using Dictionary and Functions

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved!")

def show_contacts():
    print("\n--- Contact List ---")
    for name, phone in contacts.items():
        print(name, ":", phone)

# Main Program
add_contact()
show_contacts()
