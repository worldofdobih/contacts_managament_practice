import json

def add_person():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
     for index, person in enumerate(people):
        print(f"{index +1 }.{person['name']}|{person['age']}|{person['email']}")


def delete_contact(people):
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

    people.pop(number - 1)
    print("Person deleted. ")


def search(people):
    search_name = input("Enter name for search: ").lower()
    result = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)

    display_people(result)

print("Welcometo contact managament system.")
print()

people = []

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size is: ",len(people))
    command = input("You can 'add', 'delete, or 'search' and 'q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added. ")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command. ")


with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)