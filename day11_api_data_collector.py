import requests

print("       API DATA COLLECTOR")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print()
print("Status Code:", response.status_code)

users = response.json()

print()
print("USER REPORT")

for user in users:
    print()
    print("Name:", user["name"])
    print("Email:", user["email"])

print()
print("=================================")