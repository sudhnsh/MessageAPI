from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from Twilio import *
from starlette.responses import RedirectResponse
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {'status':'OK'}

@app.get("/")
def index():
    return RedirectResponse("/docs")


@app.get("/{message_to_send}/{phone_num_to}")
def message(message_to_send,phone_num_to):
    phone_num_to='+91'+phone_num_to
    message = client.messages \
                .create(
                     body=message_to_send,
                     from_=phone_number,
                     to=phone_num_to
                 )
    if message.error_code==None:
        return {'Status':{message.status},'Message_ID':{message.sid}}
    else:
        return {'Error':{message.error_code},'Error_msg':{message.error_message}}
    
        
        