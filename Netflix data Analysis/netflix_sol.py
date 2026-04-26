import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv',)

#clean data
df=df.dropna(subset=['type','release_year','rating','country','duration'])

# Q How Many Movies VS TV Shows Through Bar Chart
type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number Of Movies VS TV Shows On netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Movies_VS_TVShow.png')
plt.show()

# Q What is The Percentage Of each Content Rating Through Pie Chart
rating_count=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage Of Each Content Rating')
plt.tight_layout()
plt.savefig('Content_Rating_Pie.png')
plt.show()


# Q How has The Number Of Releases changed Over The  Years
releases_count=df['release_year'].value_counts()
plt.figure(figsize=(10,8))
plt.plot(releases_count.index,releases_count.values,color='green',marker='o')
plt.title('Number Of Releases changed Over The  Years')
plt.xlabel('Years')
plt.ylabel('Number Of Releases')
plt.tight_layout()
plt.savefig('No._Of_Release_Over_Year .png')
plt.show()

# Q What is The Distribution Of Movie Duration Through Histrogram
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=20,color='purple',edgecolor='black')
plt.title('Distribution Of Movie Duration ')
plt.xlabel('Duration')
plt.ylabel('Number Of Movies')
plt.tight_layout()
plt.savefig('Movie_Duration_Histogram.png')
plt.show()

# Q Relation Between Release Year and Number Of Shows Through Scatter Plot
release_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_count.index,release_count.values, color='red')
plt.title(' Relation Between Release Year and Number Of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number Of Shows')
plt.tight_layout()
plt.savefig('Release_year_Scatter.png')
plt.show()

# Q Top 10 Countries With The Highest Number of Shows Through Bar Chart
country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='blue')
plt.title('Top 10 Countries With The Highest Number of Shows Through Bar Chart')
plt.xlabel('Release Year')
plt.ylabel('Number Of Shows')
plt.tight_layout()
plt.savefig('Top_10_countries.png')
plt.show()

# Q Compare Multiple Plots Together like Movies and TV Shows By Year Through Subplot
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2,figsize=(12,8))

# first subplot:movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of movies')

# second subplot:tvshow
ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='red')
ax[1].set_title('TV Show released per year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

plt.suptitle('Comparison Between TV Show and Movies By Years')
plt.tight_layout()
plt.savefig('Subplot_Moviesand_tvshow.png')
plt.show()