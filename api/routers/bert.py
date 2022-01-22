from fastapi import APIRouter
from api.bert.bert import BertAPI
import api.schemas.bert as bert_schema


router = APIRouter()
bert = BertAPI()
bert.load("/Users/uehatakosuke/dev_es/backend/api/bert/model")

@router.post("/bert")
async def predict_bert(text:bert_schema.BertPredict ) -> bert_schema.BertPredictResponse:
  print("正規化開始")
  text = bert.normalize(text.text)
  print(text)
  print("予測開始")
  res = bert.predict([text])
  print("予測終了")
  print(res)
  return  res