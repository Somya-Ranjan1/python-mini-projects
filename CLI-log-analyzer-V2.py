logs = []
valid_levels = ["INFO", "ERROR", "WARNING"]

print("Enter logs in format: LEVEL: message (type 'exit' to stop)\n")

while True:
    user_input = input("Enter log: ").strip()

    if user_input.lower() == "exit":
        break

    log_upper = user_input.upper()

    if not any(level in log_upper for level in valid_levels):
        print("❌ Invalid log! Use INFO, ERROR, or WARNING.\n")
        continue

    logs.append(log_upper)


# Counting
counts = {"INFO": 0, "ERROR": 0, "WARNING": 0}

for log in logs:
    for level in counts:
        if level in log:
            counts[level] += 1


# Output
total = len(logs)

print("\n📊 Log Summary:")
for level, count in counts.items():
    print(f"{level}: {count}")

if total > 0:
    print(f"\nTotal Logs: {total}")
    for level, count in counts.items():
        print(f"{level} %: {(count/total)*100:.1f}%")