import requests
from random import randint


URL = "http://34.238.250.217:8000/"
charType = ""
prevDict = {}

def retrieveCharacterAction(type: str) -> dict:
    try:
        response = requests.get("http://34.238.250.217:8000/"+type)
    except:
        return None

    return response.json()

def getMessage(type: str) -> str:
    global charType
    global prevDict
    if ((charType != str) or (charType == "")):
        message_type = retrieveCharacterAction(type)
        if (message_type == None):
            return None
        charType = str
        prevDict = message_type
    

    try:
        response = requests.get("http://34.238.250.217:8000/"+type+"/"+message_type[str(randint(0,len(prevDict)))])
    except:
        return None
    return response.json()[str(randint(0,len(response)))]


