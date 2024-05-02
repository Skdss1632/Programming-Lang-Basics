# # script to print first 10 natural numbers in reverse order.
# i = 10
# while i > 0:
#  print(i)
#  i -= 1




class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

contacts = []

def add_contact():
    print("\nAdd Contact")
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    new_contact = Contact(name, phone_number)
    contacts.append(new_contact)
    print("Contact added successfully.")

def view_all_contacts():
    print("\nAll Contacts")
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

def search_contact():
    print("\nSearch Contact")
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
            found = True
    if not found:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
