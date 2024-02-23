
import sys

from celery import Celery
from fastapi import FastAPI
from app.api.prediction.routers.prediction import router as prediction_router 

app = FastAPI(   
        title="ZypherAI",
        description="Sych Interview Assessment ",
        version="0.0.1",
        contact={
            "name": "Saad Khan",
            "email": "msaaddev@gmail.com",
        }
    ) 

app.include_router(prediction_router)

