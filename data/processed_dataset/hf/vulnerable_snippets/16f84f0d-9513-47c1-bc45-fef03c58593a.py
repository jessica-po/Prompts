import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error occurred: ", e)

def main():
    url = "http://example.com/api"
    data = fetch_data(url)
    print(data)

if __name__ == "__main__":
    main()
