# https://codeshare.io/j0l0lL
import requests

types = set()
for _ in range(10):
    data = requests.get("https://official-joke-api.appspot.com/jokes/ten").json()
    for joke in data:
        types.add(joke["type"])
for type in types:
    print(f'10 Jokes of type "{type}":')
    print()
    for joke in requests.get(
        f"https://official-joke-api.appspot.com/jokes/{type}/ten"
    ).json():
        print(joke["setup"], joke["punchline"])
        print()
    print()