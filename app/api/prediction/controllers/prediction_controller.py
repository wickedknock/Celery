from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.api.prediction.services import prediction_service
from app.api.prediction.schemas import prediction_schema
from app.api.prediction.services.prediction_service import predict_model_async

# The predict controller will handle which service to call based on the value of async_mode Header
def predict(asyncMode:str,body:prediction_schema.PredictionRequest)->prediction_schema.PredictionResponse:
    if asyncMode == None:
        return prediction_service.predict_model_sync(body)
    else:
        capitalizedBool = asyncMode.capitalize()
        if capitalizedBool == "True":
            input = body.input
            task = predict_model_async.delay(input)
            return prediction_schema.PredictionResponse(message='Request received. Processing asynchronously.',prediction_id=task.id)
        else:
            return prediction_service.predict_model_sync(body)  
      
    
    
def get_predict(prediction_id:str)->prediction_schema.PredictionResponse:
    return prediction_service.get_prediction_result(prediction_id)