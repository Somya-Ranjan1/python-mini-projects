import requests

# list of APIs to check
urls = [
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://invalid-url-test-123.com"
]

print("Checking APIs...\n")

for url in urls:
    try:
        response = requests.get(url)
        print(f"{url} → {response.status_code}")
    except:
        print(f"{url} → FAILED")