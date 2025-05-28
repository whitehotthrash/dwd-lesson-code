class DungeonError(Exception):
    pass

# TODO: define SecretDoorError subclassing DungeonError

def open_secret_door(code):
    # TODO: if code != "XYZ", raise SecretDoorError("Wrong secret code!")
    print("Secret door opens!")
