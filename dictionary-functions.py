# Dictionary Functions

# You are making a phonebook. The contacts are stored in a dictionary, where the key is the name and the value is a list, representing the number and the email of the contact.
# You need to implement search: take the name of the contact as input and output the email.
# If the contact is not found, output "Not found".
# Note, that the email is the second element of the list.

contacts = { 
    "David": ["123-321-88", "david@test.com"], 
    "James": ["241-879-093", "james@test.com"], 
    "Bob": ["987-004-322", "bob@test.com"], 
    "Amy": ["340-999-213", "a@test.com"] 
} 
 
name=input()
if name in contacts:
    print(contacts[name][1])
else:
    print("Not found")
