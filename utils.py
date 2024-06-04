import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from gensim.models import Word2Vec, KeyedVectors
import nltk
from tqdm import tqdm

def getVectors(model, dataset, embeddingsSize):
  singleDataItemEmbedding=np.zeros(embeddingsSize)
  vectors=[]
  for dataItem in tqdm(dataset, total=len(dataset)):
    wordCount=0
    for word in dataItem:
      if word in model.wv.key_to_index:
        singleDataItemEmbedding=singleDataItemEmbedding+model.wv[word]
        wordCount=wordCount+1

    singleDataItemEmbedding=singleDataItemEmbedding/wordCount
    vectors.append(singleDataItemEmbedding)
  return vectors