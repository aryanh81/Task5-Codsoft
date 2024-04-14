class Contact:
    
    def _init_(self):
        self.contacts = []
    
    def addContact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully")
        
    def viewContacts(self):
        if len(self.contacts) == 0:
            print("No contacts")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']} Phone number: {contact['phone']}")
    
    def searchContact(self, identifier):
        if len(self.contacts) == 0:
            print("No contacts")
        else:
            found = False
            for contact in self.contacts:
                if contact['phone'] == identifier or contact['name'] == identifier:
                    print(f"Name: {contact['name']} Phone number: {contact['phone']}")
                    found = True
            if not found:
                print("No matching contact found")
                    
    def updateContact(self, identifier):
        found = False
        for contact in self.contacts:
            if contact["phone"] == identifier or contact["name"] == identifier:
                contact["name"] = input("Update name: ")
                contact["phone"] = input("Update phone: ")
                contact["email"] = input("Update email: ")
                contact["address"] = input("Update address: ")
                print("Contact Updated")
                found = True
        if not found:
            print("No matching contact found")
    
    def deleteContact(self, identifier):
        found = False
        if len(self.contacts) == 0:
            print("No contacts")
        else:
            for contact in self.contacts:
                if contact["phone"] == identifier or contact["name"] == identifier:
                    self.contacts.remove(contact)
                    print("Contact deleted")
                    found = True
        if not found:
            print("No matching contact found")
            
def menu():
    print("Contact Book:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    ct = Contact()
    
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            ct.addContact()
        elif choice == 2:
            ct.viewContacts()
        elif choice == 3:
            identifier = input("Enter name/phone to search: ")
            ct.searchContact(identifier)
        elif choice == 4:
            identifier = input("Enter name/phone to update: ")
            ct.updateContact(identifier)
        elif choice == 5:
            identifier = input("Enter name/phone to delete: ")
            ct.deleteContact(identifier)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Try again")
        
main()
