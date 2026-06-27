import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        categories = user_data["categories"]
        content = user_data["content"]
        return categories, content

    else:
        raise Exception("Failed to fetch joke")      


def main():
    try:
        categories, content = fetch_random_user_freeapi()
        print(f"Categories: {categories} \nJoke: {content}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()