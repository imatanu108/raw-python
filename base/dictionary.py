a = {
    "key": "value",
    "marks": 100,
    "fruits": ["apple", "mango", "pineapple"],
    "user": {
        "name": "Alex",
        "age": 27,
        "skills": ["front-end dev", "back-end dev", "graphics designing"],
        "email": "alex@email.com",
    },
}

print(a["user"]["name"])

a["country"] = "USA"

print(a.items())
print(a.keys())
print(a.values())
