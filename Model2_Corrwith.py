import numpy as np
import pandas as pd

df_rating = pd.read_csv('ratings.csv')
# print(df_rating.head(3))
# print(df_rating.isnull().sum())
# print(df_rating.shape)

df_book = pd.read_csv('books.csv')
# print(df_book.isnull().sum())
# print(df_book.head(3))
# print(df_book.shape)
# print(df_book.columns)

book_titles = df_book[['book_id','title','original_title','authors']]
df = pd.merge(df_rating,book_titles, on='book_id')
# print(df.head())
# print(df.shape)
# print(df.isnull().sum())

# df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
# df.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
# print(ratings.head())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
# print(ratings.head())

book_matrix = df.pivot_table(index='user_id',columns='title',values='rating')
# print(book_matrix.head())
# print(ratings.sort_values('num of ratings',ascending=False).head(10))
# print(ratings.head())

andi_user_ratings1 = book_matrix['The Hunger Games (The Hunger Games, #1)']
budi_user_ratings1 = book_matrix["Harry Potter and the Sorcerer's Stone (Harry Potter, #1)"]
ciko_user_ratings1 = book_matrix["Robots and Empire (Robot #4)"]
dedi_user_ratings1 = book_matrix["A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam"]
ello_user_ratings1 = book_matrix["The Story of Doctor Dolittle (Doctor Dolittle, #1)"]

similiar_to_andi1 = book_matrix.corrwith(andi_user_ratings1)
similiar_to_budi1 = book_matrix.corrwith(budi_user_ratings1)
similiar_to_ciko1 = book_matrix.corrwith(ciko_user_ratings1)
similiar_to_dedi1 = book_matrix.corrwith(dedi_user_ratings1)
similiar_to_ello1 = book_matrix.corrwith(ello_user_ratings1)

corr_andi1 = pd.DataFrame(similiar_to_andi1,columns=['Correlation'])
corr_andi1.dropna(inplace=True)

corr_budi1 = pd.DataFrame(similiar_to_budi1,columns=['Correlation'])
corr_budi1.dropna(inplace=True)

corr_ciko1 = pd.DataFrame(similiar_to_ciko1,columns=['Correlation'])
corr_ciko1.dropna(inplace=True)

corr_dedi1 = pd.DataFrame(similiar_to_dedi1,columns=['Correlation'])
corr_dedi1.dropna(inplace=True)

corr_ello1 = pd.DataFrame(similiar_to_ello1,columns=['Correlation'])
corr_ello1.dropna(inplace=True)

# print(corr_andi1.head())
# print(corr_andi1.sort_values('Correlation',ascending=False).head(5))

corr_andi1 = corr_andi1.join(ratings['num of ratings'])
corr_budi1 = corr_budi1.join(ratings['num of ratings'])
corr_ciko1 = corr_ciko1.join(ratings['num of ratings'])
corr_dedi1 = corr_dedi1.join(ratings['num of ratings'])
corr_ello1 = corr_ello1.join(ratings['num of ratings'])

# print(corr_andi1.head())

print('Buku bagus untuk Andi :')
print(corr_andi1[corr_andi1['num of ratings']>1000].sort_values('Correlation',ascending=False).head()[1:])
print('\n')

print('Buku bagus untuk Budi :')
print(corr_budi1[corr_budi1['num of ratings']>1000].sort_values('Correlation',ascending=False).head()[1:])

print('Buku bagus untuk Ciko :')
print(corr_ciko1[corr_ciko1['num of ratings']>1000].sort_values('Correlation',ascending=False).head()[1:])
print('\n')

print('Buku bagus untuk Dedi :')
print(corr_dedi1[corr_dedi1['num of ratings']>1000].sort_values('Correlation',ascending=False).head()[1:])
print('\n')

print('Buku bagus untuk Ello :')
print(corr_ello1[corr_ello1['num of ratings']>1000].sort_values('Correlation',ascending=False).head()[1:])
print('\n')