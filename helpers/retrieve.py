import requests
from random import randint


URL = "http://34.238.250.217:8000/"
charType = ""
prevDict = {}
prevResponse = 0

def retrieveCharacterAction(type: str) -> dict:
    try:
        response = requests.get("http://34.238.250.217:8000/"+type)
    except:
        return None

    return response.json()

def getMessage(type: str) -> str:
    global charType
    global prevDict
    global prevResponse
    if ((charType != str) or (charType == "")):
        message_type = retrieveCharacterAction(type)
        if (message_type == None):
            return None
        charType = str
        prevDict = message_type
    

    try:
        key = randint(0,len(prevDict)-1)
        if (key == prevResponse):
            key = (key+1)%len(prevDict)
        prevResponse = key
        link = "http://34.238.250.217:8000/"+type+"/"+prevDict[str(key)]
        
        response = requests.get(link)
    except:
        return None
    response = response.json()
    return response[str(randint(0,len(response)-1))]


