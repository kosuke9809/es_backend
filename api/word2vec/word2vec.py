import gensim

class Word2VecAPI:
  def __init__(self):
    self.word2vec = None
  def load(self):
    self.word2vec = gensim.models.word2vec.KeyedVectors.load_word2vec_format('/Users/uehatakosuke/dev_es/backend/api/word2vec/model.vec', binary=False)
    
  def similarity_words(self,keyword:str,word:str) -> str:
    word2vec = self.word2vec
    res = word2vec.similarity(keyword,word)
    return res
    

