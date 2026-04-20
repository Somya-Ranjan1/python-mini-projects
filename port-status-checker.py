ports = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP"
}

while True:
    user_input = input("Enter port number (or type 'exit'): ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    port = int(user_input)

    if port in ports:
        print(f"Port {port} is commonly used for {ports[port]}")
    else:
        print(f"Port {port} is unknown")