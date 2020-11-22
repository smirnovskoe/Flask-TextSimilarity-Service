from sentence_transformers import SentenceTransformer
import torch
import numpy as np
from scipy import spatial

def text2list(txt):
    return txt.split('.')

def text_similarity(text1, text2, model):
    text1_sent = text2list(text1)
    text2_sent = text2list(text2)

    embeddings1 = model.encode(text1_sent, convert_to_tensor=True)
    embeddings2 = model.encode(text2_sent, convert_to_tensor=True)

    result = 1 - spatial.distance.cosine(embeddings1.mean(axis=0), embeddings2.mean(axis=0))
    return result  

model_name = 'distiluse-base-multilingual-cased-v2'
model_multiling = SentenceTransformer(model_name)
