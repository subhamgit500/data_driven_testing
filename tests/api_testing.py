import requests

# response = requests.get("https://fakestoreapi.com/products")
# print(response.status_code)
# print(response.text)

payload = {
 "title": "foo",
 "body": "bar",
 "userId": 1
 }

response1 = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload)

print(response1.status_code)
print(response1.json())
