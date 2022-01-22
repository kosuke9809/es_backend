from pydantic import BaseModel
from typing import Dict,List

class InputMecab(BaseModel):
  text : str

class ResposeMecab(BaseModel):
  # res:Dict[str,List[str]]
  res:List[Dict[str,str or int]]