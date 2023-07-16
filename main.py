from fastapi import FastAPI

#Setting up the FastAPI object
app = FastAPI()

#Setting up home route for API requests
@app.get("/")
def home():
    return {"message": "Hello World"}

#Creating an API endpoint for all pokemon
@app.get("/pokemon")
def GetAllPokemon():
    #TO-DO: implement this
    return