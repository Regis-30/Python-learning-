# Exercise: writing user intered names in a ist
names_list = []

while True:
    name = input("Enter a name (type 'done' to finesh): ")
    if name.lower() == "done":
        break
    names_list.append(name)

print("The list of names:")
for name in names_list:
    print("~", name)
