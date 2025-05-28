class DungeonError(Exception):
    pass

class SecretDoorError(DungeonError):
    """Raised when secret code is wrong."""

def open_secret_door(code):
    if code != "XYZ":
        raise SecretDoorError("Wrong secret code!")
    print("Secret door opens!")

