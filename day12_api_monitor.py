import requests
import time


print(" API MONITOR")


url = "https://jsonplaceholder.typicode.com/users"

start_time = time.time()

response = requests.get(url)

end_time = time.time()

response_time = end_time - start_time

if response.status_code == 200:
    status = "ONLINE"
else:
    status = "FAILED"

print()
print("========== MONITORING REPORT ==========")
print()
print("API:", url)
print("Status Code:", response.status_code)
print("Response Time:", round(response_time, 2), "seconds")
print("Status:", status)
print()
