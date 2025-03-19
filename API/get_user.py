import requests

def fetch_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_email = data["data"]["data"][0]["email"]
        return user_email
    else:
        raise Exception("Failed to fetch user email.")

def main():
    try:
        email = fetch_users()
        print("User email is", email)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()