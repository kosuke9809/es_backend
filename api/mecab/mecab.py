import re
import MeCab
from typing import List,Dict

class MeCabAPI:
  def __init__(self):
    self.mecab = None
  
  def load(self):
    self.mecab = MeCab.Tagger()

  def preprocessing_text(self,text:str) -> str:
    #改行，半角スペース，全角スペースを削除
    text = re.sub('\r','',text)
    text = re.sub('\n','',text)
    text = re.sub('　','',text)
    text = re.sub(' ','',text)
    return text

  def tokenizer_mecab(self,text:str) -> Dict[str,List[str]]:
    mecab = self.mecab
    keywords = [line.split()[0] for line in mecab.parse(text).splitlines() if "名詞" in line.split()[-1]]
    l = []
    for word in keywords:
      dict = {}
      num = keywords.count(word)
      dict["text"] = word
      dict["value"] = num
      if dict not in l:
        l.append(dict)
    # res = {"data":keywords}
    res = l
    return res
