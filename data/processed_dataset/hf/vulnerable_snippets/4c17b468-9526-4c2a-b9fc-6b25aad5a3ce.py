import os
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

def save_data(data):
    with open('data.txt', 'w') as f:
        f.write(data)

def main():
    url = input("Enter a URL: ")
    data = fetch_data(url)
    save_data(data)

if __name__ == "__main__":
    main()
