import os

while True:
    var = input("Enter environment variable (or type exit): ")

    if var.lower() == "exit":
        break

    value = os.getenv(var)

    if value:
        print(f"{var} = {value}\n")
    else:
        print("Variable not found\n")