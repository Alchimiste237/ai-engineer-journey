import requests
url = "https://jsonplaceholder.typicode.com/posts"

reponse = requests.get(url)
data = reponse.json()
# print(data[0])

for user in data:
    print(f"User ID: {user['userId']}, Title: {user['title']}")

reponse = requests.post(url, json={"title": "New Post", "body": "This is a new post.", "userId": 1})
if reponse.status_code == 201:
    print("Post created successfully:", reponse.json())