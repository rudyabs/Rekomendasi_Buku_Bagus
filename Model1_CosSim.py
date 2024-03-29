import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.read_csv('books.csv',encoding='utf8')
# print(books.head())
# print(books.isnull().sum())
# print(books.columns)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

tfidf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['authors'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# print(cosine_sim)

titles = books['title']
indices = pd.Series(books.index, index=books['title'])

def rekomendasi(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    book_indices = [i[0] for i in sim_scores]
    return titles.iloc[book_indices]


print('Buku Buku bagus untuk Andi:')
print(rekomendasi("The Hunger Games (The Hunger Games, #1)").head(5))
print('\n')

print('Buku Buku bagus untuk Budi:')
print(rekomendasi("Harry Potter and the Sorcerer's Stone (Harry Potter, #1)").head(5))
print('\n')

print('Buku Buku bagus untuk Ciko:')
print(rekomendasi("Robots and Empire (Robot #4)").head(5))
print('\n')

print('Buku Buku bagus untuk Dedi:')
print(rekomendasi("Bridget Jones's Diary (Bridget Jones, #1)").head(5))
print('\n')

print('Buku Buku bagus untuk Ello:')
print(rekomendasi("A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam").head(5))
print('\n')

