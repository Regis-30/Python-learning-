# creating a password to grant access to the user
password = ""

while password != "12345":
    password = input("What's the password: ")
    if password == "":
        print("Access denied")
    elif password != "12345":
        print("wrong password")
print("Access granted")
