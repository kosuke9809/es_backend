import collections
from fastapi import APIRouter
from api.mecab.mecab import MeCabAPI
from api.word2vec.word2vec import Word2VecAPI
import api.schemas.mecab as mecab_schema

router = APIRouter()
mecab = MeCabAPI()
word2vec = Word2VecAPI()

mecab.load()
word2vec.load()

@router.post("/mecab")
async def mecab_parse(text:mecab_schema.InputMecab) -> mecab_schema.ResposeMecab:
  mecab_text = mecab.preprocessing_text(text.text)
  keywords ,words= mecab.tokenizer_mecab(mecab_text)
  
  c = collections.Counter(words)
  values, _ = zip(*c.most_common(5))
  
  score = 0
  weight = {0:0.4,1:0.3,2:0.15,3:0.1,4:0.05}
  for k,v in weight.items():
    tmp= word2vec.similarity_words('向上心',values[k]) * 0.2
    score += tmp
    print(values[k])
    print(tmp)
  
  print(score,'合計')

  return keywords