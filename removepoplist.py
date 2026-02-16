# using, remove(), pop() on list items
tasks = ["study", "sleep", "work", "eat", "cleaning"]
if "eat" in tasks:
    tasks.remove("eat")
tasks.pop(2)
print(tasks)
