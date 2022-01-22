from pydantic import BaseModel
from typing import Dict,List
class BertPredict(BaseModel):
  text : str
  
class BertPredictResult(BaseModel):
  res: Dict[int,int]
  
class BertPredictResponse(BaseModel):
  res: Dict[str,List[int]]