from random import randint

def random_user_id() -> str:
    characteres = "abcdefghijklmnopqrstuwxyz123456789"
    id = ""
    for _ in range(6):
        aux = randint(0, len(characteres) - 1)
        id += characteres[aux]

    return id

print(random_user_id())
