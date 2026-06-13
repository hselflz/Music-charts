import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
       "mysql+pymysql://root:75537342@localhost/music_charts"
)

df = pd.read_sql(
    "SELECT * FROM music_charts",
    con=engine
)
print(df.info())

df.info()

song_top = df.groupby("song_title")[("streams")].sum()
song_top = song_top.sort_values(ascending=False).head(10)
print(song_top)
print(f"Song with most streams: {song_top.index[0]}, with {song_top.iloc[0]} streams")

artist_top = df.groupby("artist")[("streams")].sum()
artist_top = artist_top.sort_values(ascending=False)
print(f"Artist with most streams: {artist_top.index[0]}, with {artist_top.iloc[0]} streams")

top_country = df.groupby("country")[("streams")].sum()
top_country = top_country.sort_values(ascending=False)
print(f"Country with most streams: {top_country.index[0]}, with {top_country.iloc[0]} streams")

consistent_song = df.groupby("song_title")[("chart_date")].count()
consistent_song = consistent_song.sort_values(ascending=False)
print(f"Most consistent song: {consistent_song.index[0]}, with {consistent_song.iloc[0]} weeks on the chart")

consistent_artist = df.groupby("artist")[("chart_date")].count()
consistent_artist = consistent_artist.sort_values(ascending=False)
print(f"Most consistent artist: {consistent_artist.index[0]}, with {consistent_artist.iloc[0]} weeks on the chart")