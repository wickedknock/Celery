import random
import time
from celery.app import Celery
from fastapi.responses import JSONResponse
from app.api.prediction.schemas import prediction_schema


# Services will handle all the business logic

redis_url = "redis://redis:6379"

app = Celery(__name__, broker=redis_url, backend=redis_url)

def predict_model_sync(body: prediction_schema.PredictionRequest)->prediction_schema.PredictionResponse:
    time.sleep(random.randint(8, 15)) 
    result = str(random.randint(100, 10000))
    return prediction_schema.PredictionResponse(input=body.input, result=result)
    
    


def get_prediction_result(prediction_id: str)->prediction_schema.PredictionResponse:
    task = predict_model_async.app.AsyncResult(prediction_id)
    if task.task_id is None:
        return prediction_schema.PredictionResponse(error="Prediction ID not found.")
    elif task.status == "PENDING":
        return prediction_schema.PredictionResponse(error="Prediction is still being processed.")
    elif task.status == "SUCCESS":
        result = task.result
        output_data = {"input": "Sample input data for the model", "result":result['result'] }
        response_model = prediction_schema.PredictionResponse(prediction_id=task.task_id, output=output_data)
        return JSONResponse(content=response_model.to_dict_exclude_none(),status_code=201)
    elif task.status == "FAILURE":
        return prediction_schema.PredictionResponse(error="Task Failed")
   

@app.task(name="predict_model_async")
def predict_model_async(input:str)->dict[str,str]:
    time.sleep(random.randint(8, 15)) 
    result = str(random.randint(100, 10000))
    data = {"input": input, "result": result}
    return data
   
   