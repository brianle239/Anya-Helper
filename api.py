from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Go To Sleep Robert"}

@app.get("/sleep")
async def root():
    return {"msg1":"Good Night", "msg2": "Sweet Dreams", "msg3": "Good Luck Tomorrow"}

@app.get("/dissapointed")
async def root():
    return {"msg1":"", "msg": "Sweet Dreams"}

@app.get("/watching")
async def root():
    return {"msg1":"I See you!", "msg2": "Get Back To Work Now", "msg3": "I am always watching"}
    