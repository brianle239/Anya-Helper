from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Go To Sleep Robert"}

@app.get("/mom")
async def root():
    return {0:"sleep", 1: "dissapointed", 2: "watching"}

@app.get("/mom/sleep")
async def root():
    return {0:"Good Night", 1: "Sweet Dreams", 2: "Good Luck Tomorrow"}

@app.get("/mom/dissapointed")
async def root():
    return {0:"Why you no doctor yet", 1: "I'm not mad, just Dissapointed", 2: "Why are you not like your cousing"}

@app.get("/mom/watching")
async def root():
    return {0:"I See you!", 1: "Get off your phone NOW", 2: "I am always watching"}


@app.get("/dad/sleep")
async def root():
    return {0:"zzZZ", 1: "Be QUIET! I Work tomorrow", 2: "Good Night"}

@app.get("/dad/encouragement")
async def root():
    return {0:"I'm proud of you", 1: "Good Job", 2: "Keep working hard"}

@app.get("/dad/joke")
async def root():
    return {0:"Going to get milk", 1: "Knock Knock", 2: "Your mom does it better"}




