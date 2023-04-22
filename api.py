from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Go To Sleep Robert"}

@app.get("/sleep")
async def root():
    return {0:"Good Night", 1: "Sweet Dreams", 2: "Good Luck Tomorrow"}

@app.get("/dissapointed")
async def root():
    return {0:"...", 1: "I'm not mad, just Dissapointed", 2: "Get back to work"}

@app.get("/watching")
async def root():
    return {0:"I See you!", 1: "Get Back To Work Now", 2: "I am always watching"}
    