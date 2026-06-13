import pandas as pd
from sqlalchemy import create_engine

password_git = input("Enter your MySQL password: ")
engine = create_engine(
       "mysql+pymysql://root:" + password_git + "@localhost/music_charts"
)

df = pd.read_sql(
    "SELECT * FROM music_charts",
    con=engine
)
print(df.info())

df.info()

def top_songs(df):
    song_top = df.groupby("song_title")[("streams")].sum()
    song_top = song_top.sort_values(ascending=False)    
    print(f"Song with most streams: {song_top.index[0]}, with {song_top.iloc[0]} streams")
top_songs(df)

def top_artist(df):
    artist_top = df.groupby("artist")[("streams")].sum()
    artist_top = artist_top.sort_values(ascending=False)
    print(f"Artist with most streams: {artist_top.index[0]}, with {artist_top.iloc[0]} streams")
top_artist(df)

def top_country(df):
    country_top = df.groupby("country")[("streams")].sum()
    country_top = country_top.sort_values(ascending=False)
    print(f"Country with most streams: {country_top.index[0]}, with {country_top.iloc[0]} streams")
top_country(df)

def most_consistent_song(df):
    consistent_song = df.groupby("song_title")[("chart_date")].count()
    consistent_song = consistent_song.sort_values(ascending=False)
    print(f"Most consistent song: {consistent_song.index[0]}, with {consistent_song.iloc[0]} weeks on the chart")
most_consistent_song(df)

def most_consistent_artist(df):
    consistent_artist = df.groupby("artist")[("chart_date")].count()
    consistent_artist = consistent_artist.sort_values(ascending=False)
    print(f"Most consistent artist: {consistent_artist.index[0]}, with {consistent_artist.iloc[0]} weeks on the chart")
most_consistent_artist(df)

def analyze_popularity_factors(df):
    correlation = df.groupby("streams")[["danceability", "valence","energy"]].sum()
    print(correlation)
analyze_popularity_factors(df)