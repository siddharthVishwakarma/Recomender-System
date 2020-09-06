#importing neccesary packages
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

da1 = pd.read_csv('links.csv')
da2 = pd.read_csv('movies.csv')
da3 = pd.read_csv('ratings.csv')
da4 = pd.read_csv('tags.csv')


dataframe = pd.merge(da2,da3).drop(['genres','timestamp'],axis=1)

#creating a pivot table
pivot_table = dataframe.pivot_table(index='userId',columns='title',values='rating')

#creating mean ratings data
ratings = pd.DataFrame(dataframe.groupby('title')['rating'].mean())

#creating number of ratings data
ratings['number_of_ratings'] = dataframe.groupby('title')['rating'].count()

#Plotting the jointplot
import seaborn as sns
sns.jointplot(x='rating', y='number_of_ratings', data = ratings)

#Most rated movies
ratings.sort_values('number_of_ratings', ascending=False)

#making recomendation on movie Silence of the Lambs.

#Fetching ratings for movie
user_rating = pivot_table['Silence of the Lambs, The (1991)']

#Finding the correlation with different movies
similar_to_movie = pivot_table.corrwith(user_rating)

#creating a threshold for minimum number of ratings-

#creating dataframe to bring in #of ratings
corr_lamb = pd.DataFrame(similar_to_movie, columns=['Correlation'])
corr_lamb.dropna(inplace=True)

#Bringining in ratings
corr_lamb = corr_lamb.join(ratings['number_of_ratings'])

#Recomendation
corr_lamb[corr_lamb['number_of_ratings'] > 30].sort_values(by='Correlation', ascending=False)





















