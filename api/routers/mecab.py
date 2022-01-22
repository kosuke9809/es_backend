from fastapi import APIRouter
from api.mecab.mecab import MeCabAPI
import api.schemas.mecab as mecab_schema
router = APIRouter()

mecab = MeCabAPI()
mecab.load()


@router.post("/mecab")
async def mecab_parse(text:mecab_schema.InputMecab) -> mecab_schema.ResposeMecab:
  mecab_text = mecab.preprocessing_text(text.text)
  keywords = mecab.tokenizer_mecab(mecab_text)
  print(keywords)
  return keywords