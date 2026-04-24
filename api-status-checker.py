import requests

while True:
    url = input("Enter API URL (or type exit): ")

    if url.lower() == "exit":
        break

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except:
        print("Failed to connect to the API")