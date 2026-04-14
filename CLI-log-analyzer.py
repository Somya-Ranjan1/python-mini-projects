logs = []

while True:
    user_input = input("Enter log (type 'exit' to stop): ")
    
    if user_input.lower() == "exit":
        break
    
    logs.append(user_input.upper())

info_count = 0
error_count = 0
warning_count = 0

for log in logs:
    if "INFO" in log:
        info_count += 1
    elif "ERROR" in log:
        error_count += 1
    elif "WARNING" in log:
        warning_count += 1

print("Log Summary:")
print("INFO:", info_count)
print("ERROR:", error_count)
print("WARNING:", warning_count)