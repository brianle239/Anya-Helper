import requests
from random import randint


URL = r"http://34.238.250.217:8000/"
charType = ""
prevDict = {}
prevResponse = 0

def retrieveCharacterAction(type: str) -> dict:
    try:
        response = requests.get(URL+type, timeout=5)
    except:
        return None
    return response.json()

def getMessage(type: str) -> str:
    global charType
    global prevDict
    global prevResponse
    if ((charType != type) or (charType == "")):
        message_type = retrieveCharacterAction(type)
        if (message_type == None):
            return ""
        charType = type
        prevDict = message_type
    

    try:
        key = randint(0,len(prevDict)-1)
        if (key == prevResponse):
            key = (key+1)%len(prevDict)
        prevResponse = key
        link = URL+type+"/"+prevDict[str(key)]
        
        response = requests.get(link, timeout=5)
    except:
        return ""
    response = response.json()
    return response[str(randint(0,len(response)-1))]


if __name__ == "__main__":
    print(retrieveCharacterAction("mom"))