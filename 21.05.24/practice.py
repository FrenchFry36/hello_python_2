users = [
    {"telephone_number": "1758496", "name": "Alice", "age": 30},
    {"telephone_number": "2363646", "name": "Xavier", "age": 25},
    {"telephone_number": "3124543", "name": "Bill", "age": 35},
    {"telephone_number": "4134613", "name": "Sergi", "age": 28},
    {"telephone_number": "1235255", "name": "Eve", "age": 22}
]

print(users[0]["name"])

newUserName = input("What is yuor name? ")
newUserAge = input("How old are you? ")
newUserPhone = input("Type your phone number: ")
users.append({"name": newUserName, "age": newUserAge, "telephone_number": newUserPhone})

for i in users:
    print(f"{i['name']} | {i['age']} | {i['telephone_number']}")


users.append({"telephone number": "2343547", "name": "Ivan", "age": 23})
print(users)