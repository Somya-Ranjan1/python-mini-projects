with open("logs.txt", "r") as file:
    logs = file.readlines()

counts = {"INFO": 0, "ERROR": 0, "WARNING": 0}

for log in logs:
    log = log.strip().upper()
    
    for level in counts:
        if level in log:
            counts[level] += 1

print("Log Summary:")
for level, count in counts.items():
    print(f"{level}: {count}")