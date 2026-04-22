import json

users = []

while True:
    name = input("Enter name (or type exit): ")

    if name.lower() == "exit":
        break

    email = input("Enter email: ")

    user = {
        "name": name,
        "email": email
    }

    users.append(user)

# Save to file
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("Users saved to users.json")