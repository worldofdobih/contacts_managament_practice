import json

def save_data(people, recycle_list):
    with open("contacts.json", "w") as f:
        json.dump({
            "contacts": people,
            "recycle_bin": recycle_list
            }, f, indent=4)


def add_person():
    name = input("Enter name: ")
    age = input("Enter age: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    person = {"name": name, "age":age, "phone":{"mobile":phone}, "email": email}
    return person



def add_phone(people):
    display_people(people)
    while True:
        edit_contact = input("Add number to edit. ")
        try:
            edit_contact = int(edit_contact)
            if edit_contact <= 0 or edit_contact > len(people):
                print("Invalid number, out of range. ")
            else:
                break
        except:
            print("Invalid number. ")
    title = input("Add title for number: ")
    phone_number = (input("Add number for contact: "))
    people[edit_contact - 1 ]["phone"][title] = phone_number
    print("Number added. ")

    save_data(people, recycle_list)



def display_people(people):
    for index, person in enumerate(people):
        print(f"{index +1 }.{person['name']}|{person['age']}|{person['phone']}|{person['email']}")



def delete_contact(people,recycle_list):
    display_people(people)

    while True:
        number = input("Add number to delete. ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of the range. ")
            else :
                break
        except:
            print("Invalid number. ")
    removed_contact = people.pop(number - 1) 
    recycle_list.append(removed_contact)
    print("Person moved to recycle bin. ")

    save_data(people, recycle_list)


def recycle_bin(people, recycle_list):
    if recycle_list == []:
        print("Recycle bin is empty. ")
        return
    
    for index, person in enumerate(recycle_list):
        print(f"{index +1 }.{person['name']}|{person['age']}|{person['phone']}|{person['email']}")

    while True: 
        clear_recycle = input("Do you want to clear recycle bin? yes/no").lower()
        if clear_recycle == "yes":
            recycle_list.clear()
            print("Recycle bin cleared. ")
            break
        elif clear_recycle == "no":

            restore = input("Do you want to re-store contacts? yes/no")
            if restore == "yes":
                people.extend(recycle_list)
                recycle_list.clear()
                print("Contacts restored. ")
                break
            elif restore == "no":
                break
            else: 
                print("Invalid input.only yes or no. ")
        else:
            print("Invalid input only yes or no . ") 



def search(people):
    
    result = []

    while True: 
        search_option = input("Search by name or email? n/e").lower()
        
        if search_option == "n":
            search_name = input("Enter name for search: ").lower()
            for person in people:
                name = person["name"]
                if search_name in name.lower():
                    result.append(person)
                    break
            display_people(result)
            break
        elif search_option == "e":
            search_mail = input("Enter email for search: ").lower()
            for person in people:
                email = person["email"]
                if search_mail in email.lower():
                    result.append(person)
                    break
            display_people(result)
            break
        else:
            print("Invalid option. Only enter 'n' for name or 'e' for email.")
        

def list_all_contacts(people, number_of_people):
    for index, person in enumerate(people):
        if index == number_of_people:
            return
        print(f"{index + 1 }.{person['name']}|{person['age']}|{person['phone']}|{person['email']}")
        



def sort_list(sort, people):
    if sort == "n":
        people.sort(key= lambda person:person['name'])
        
    elif sort == "a":
        people.sort(key= lambda person: int(person['age']))


def above_25(people):
    count = 0
    for person in people:
        if people['age'] > 25:
            count += 1
            print(f"{count}.{person['name']}|{person['age']}|{person['phone']}|{person['email']}")

    if count == 0 :
        print("No contact above 25 years old.")
            
            


        
            

people = []
recycle_list = []


with open("contacts.json", "r") as f:
    data = json.load(f)
    people = data.get("contacts", [])
    recycle_list = data.get("recycle_bin", [])


while True:
    print("Welcome to contact managament system.")
    print()
    print("Contact list size is: ",len(people))
    command = input("input: 'add'>>new contact, 'delete'>>contact,'search'>> for contacts, 'list'>> contacts ,'r'>show recycle-bin 'a'>add new number ,'25'>>years ols,  'q'>> quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        save_data(people, recycle_list)
        print("Person added. ")

    elif command == "delete":
        delete_contact(people, recycle_list)
       
    elif command == "r":
        recycle_bin(people, recycle_list)
        save_data(people, recycle_list)

    elif command == "search":
        #search_option = input("Search by name or email? n/e").lower()
        search(people)

    elif command == 'list':
        while True:
            try:
                number_of_people = int(input('How many people do you want to see? '))
                if number_of_people <= 0 :
                    print("Enter positive number.. ")
                else:
                    break
            except ValueError:
                print("Invalid, Enter a valid number. ")
        while True:
            sort = input("Sort by name or or age? n/a").lower()
            if sort == 'n' or sort == 'a':
                break
            else:
                print("Invalid . enter 'n' for name or 'a' for age. ")

        sort_list(sort, people)
        list_all_contacts(people, number_of_people)

    elif command == "25":
        above_25(people)
        
    elif command == "a":
        add_phone(people)
        

    elif command == "q":
        break
    else:
        print("Invalid command. ")