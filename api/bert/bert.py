import re
from time import sleep
from typing import List
import torch
from transformers import BertJapaneseTokenizer,BertForSequenceClassification
import api.schemas.bert as bert_schema

class BertAPI:
    def __init__(self):
      # model instanse
      self.model = None
      self.tokenizer = None

    def load(self,model_path):
      sleep(5)
      bert_sc = BertForSequenceClassification.from_pretrained(model_path,num_labels=2)
      tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
      DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
      model = bert_sc.to(DEVICE)
      self.tokenizer = tokenizer
      self.model = model
      
    def normalize(self,text:bert_schema.BertPredict) -> bert_schema.BertPredict:
      text = re.sub('\r','',text)
      text = re.sub('\n','',text)
      text = re.sub('　','',text)
      text = re.sub(' ','',text)
      
      return text
      
    def predict(self, text:List[bert_schema.BertPredict]) -> bert_schema.BertPredictResult:
      print("text受け取った！")
      tokenizer = self.tokenizer
      model = self.model
      encoding = tokenizer(text,max_length=350,padding='max_length',return_tensors="pt")
      encoding = {k:v for k,v in encoding.items()}
      
      with torch.no_grad():
        output = model.forward(**encoding)
      scores = output.logits
      softmax_results = torch.softmax(scores, dim=1)
      
      score = list(map(lambda score:int(score*100),softmax_results[0]))
      bert_result = {"label":[1,0],"score": [score[1],100-score[1]]}

      return bert_result