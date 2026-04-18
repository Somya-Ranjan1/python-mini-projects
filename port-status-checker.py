ports = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP"
}

port = int(input("Enter port number: "))

if port in ports:
    print(f"Port {port} is commonly used for {ports[port]}")
else:
    print(f"Port {port} is unknown or not in the list")