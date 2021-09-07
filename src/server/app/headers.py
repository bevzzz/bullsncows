# Built-in libraries
import base64


def parse_auth(auth: str):
    _, creds = auth.split(" ")
    creds_bytes = base64.b64decode(creds.encode())
    creds = creds_bytes.decode()
    return creds.split(":")
