from ctypes import Union
from typing import Any, Dict
from pydantic import BaseModel, ConfigDict, Extra

class PredictionRequest(BaseModel):
    input: str

class PredictionResponse(BaseModel):
    input: str = None
    result: str = None
    message: str = None
    prediction_id : str = None
    error : str = None
    output : Dict[str,Any] = None
    
    def to_dict_exclude_none(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}