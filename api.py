from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"HEHE HAHA"}

######## MOM ############
@app.get("/mom")
async def root():
    return {0:"sleep", 1: "dissapointed", 2: "watching", 3:"encouragement"}

@app.get("/mom/sleep")
async def root():
    return {0:"Good Night", 1: "Sweet Dreams", 2: "Good Luck Tomorrow", 3: "Ya Duermete!", 4: "Buenas Noches"}

@app.get("/mom/dissapointed")
async def root():
    return {0:"Why you no doctor yet?", 1: "I'm not mad, just Dissapointed", 2: "Why aren't you like your cousin?", 3: "Ponte las pilas", 4: "Wait till your father gets here"}

@app.get("/mom/watching")
async def root():
    return {0:"I See you!", 1: "Get off your phone NOW", 2: "I am always watching", 3: "Nomas estas con el telephono"}

@app.get("/mom/encouragement")
async def root():
    return {0:"I'm proud of you", 1: "I believe in you", 2: "I love you unconditionally", 3: "I love you", 4: "Give it your all", 5:"Echale Ganas", 6: "Te quiero", 7: "Dad would be proud"}

######## Pikachu ############

@app.get("/pikachu")
async def root():
    return {0:"sleep", 1: "disapointed", 2: "watching", 3:"encouragement", 4: "pikapika", 5: "joke"}

@app.get("/pikachu/sleep")
async def root():
    return {0:"zzZZ", 1: "pikaaa", 2: "pikaaaaa [Goodnight]"}

@app.get("/pikachu/disapointed")
async def root():
    return {0:"Pika Pi [TSK TSK TSK]", 1: "Pika!! [Be QUIET!]", 2: "Pika Pika [Your Stupid]"}

@app.get("/pikachu/watching")
async def root():
    return {0:"-_-", 1: "Pikachuuu [I see you]"}

@app.get("/pikachu/encouragement")
async def root():
    return {0:"PIKA PIKA!! [I'm proud of you]", 1: "PIKACHUU [Good Job]", 2: "PIKAA [Keep working hard]"}

@app.get("/pikachu/pikapika")
async def root():
    return {0:"Pika Pika!", 1: "Pikachu!!", 2: "Ketchup"}

@app.get("/pikachu/joke")
async def root():
    return {0:"Going to get milk", 1: "Knock Knock", 2: "Your mom does it better", 3: "Pick me Choose me", 4:"Catch em All"}

########  Professor ############

@app.get("/professor")
async def root():
    return {0:"homework", 1: "dissapointed", 2: "cheating", 3:"encouragement"}

@app.get("/professor/homework")
async def root():
    return {0:"Homework due friday!", 1: "Go to office hours", 2: "No internet for homework!"}


@app.get("/professor/dissapointed")
async def root():
    return {0:"Wow no homework done", 1: "Dissapointed", 2: "That was lower than I expected", 3:"Try Better"}


@app.get("/professor/cheating")
async def root():
    return {0:"NO CHEATING", 1: "You'll never learn if your cheat", 2: "No exceptions!", 3:"Follow the rules!"}

@app.get("/professor/encouragement")
async def root():
    return {0:"Ready..Set..Breathe..", 1: "Okay Class!", 2: "You can succeed", 3:"Almost there!"}



