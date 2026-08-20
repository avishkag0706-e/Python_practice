'''DAY 5
Contact Book '''

contacts = { }


# Add a contact
def add_contact():
    name =  input("Enter contact name: ")
    phone = input("Enter phone number: ")
    
    contacts[name]=phone
    print("contact added successfully! ")
    

# View all contacts 
def view_contacts():
    if (len(contacts)==0):
        print("no contacts found.")
    else:
        print("Contacts")    
        
        for name,phone in contacts.items():
            print("Name:",name)
            print("Phone:",phone)
            print("--------------")
            
            
            
# Search for a contact
def search_contact():
    name = input("Enter name to search:")
    
    if name in contacts:
        print("Name:",name)
        print("Phone",contacts[name])
    else:
        print("contact not found")


# Delete a contact
def delete_contact():
    name = input("Enter name to delete:")
    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("contact not found.")
    
    
# Exit
def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

  
while True:
    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View contact")
    print("3. search contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice:")
    
    if(choice=="1"):
        add_contact()
    elif choice =="2":
        view_contacts()
    elif choice =="3":
        search_contact()
    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


