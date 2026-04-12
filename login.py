print("🔐 Login to your account")

correct_username = "somya"
correct_password = "123"

for attempt in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("✅ Login successful!")
        break

    elif username != correct_username and password != correct_password:
        print("❌ Invalid username and password")

    elif username != correct_username:
        print("❌ Invalid username")

    else:
        print("❌ Invalid password")

    remaining = 2 - attempt
    if remaining > 0:
        print(f"You have {remaining} attempts left\n")
    else:
        print("🚫 Account locked!")