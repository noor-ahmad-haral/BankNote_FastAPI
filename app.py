# 1 - Importing the FastAPI class from the fastapi module.
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd



# 2 - Create app object

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

from fastapi.middleware.cors import CORSMiddleware

# Add this line to your FastAPI app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World, this is my first FastAPI"}


@app.get('/{name}')
def get_name(name:str):
    return {"Welcome to FastAPI": f"{name}"}

@app.post('/predict')
def predict_bank_note(data:BankNote):
    data = data.model_dump()
    
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note ❌"
    else:
        prediction="Its a Bank note ✅"
    return {
        'prediction': prediction}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload