from fastapi import APIRouter, Header
from app.api.prediction.controllers import prediction_controller
from app.api.prediction.schemas import prediction_schema



router = APIRouter()

@router.post("/predict" ,tags=["Prediction"],response_model_exclude_none=True)
async def prediction_route(body:prediction_schema.PredictionRequest,async_mode: str = Header(None))->prediction_schema.PredictionResponse:
    if async_mode is None or async_mode == '':
        async_mode = None
    data = prediction_controller.predict(async_mode,body)
    return data


@router.get("/predict/{prediction_id}" ,tags=["Prediction"],response_model_exclude_none=True)
async def prediction_status_route(prediction_id:str)->prediction_schema.PredictionResponse:
    data =prediction_controller.get_predict(prediction_id)
    return data
    