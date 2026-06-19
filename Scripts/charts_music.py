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

print(df.head(5))

def top_songs(df, top_n=10):
    song_top = (
        df.groupby("song_title", as_index=False)
          .agg(
              streams=("streams", "sum"),
              artist=("artist", "first"),
              country=("country", "first"),
              danceability=("danceability", "mean"),
              energy=("energy", "mean"),
              valence=("valence", "mean"),
              weeks_on_chart=("chart_date", "count")
          )
          .sort_values("streams", ascending=False)
    )
    return song_top.head(top_n)

top_songs(df)

def top_artist(df):
    artist_top = df.groupby("artist")[("streams")].sum()
    artist_top = artist_top.sort_values(ascending=False)
    print(f"Artist with most streams: {artist_top.index[0]}, with {artist_top.iloc[0]} streams")
top_artist(df)

def top_country(df, top_n=5):
    country_top = df.groupby("country")[("streams")].sum()
    country_top = country_top.sort_values(ascending=False)
    print(f"Country with most streams: {country_top.index[0]}, with {country_top.iloc[0]} streams")
    print(f"Top {top_n} countries by streams:")
    print("So the top countries are:")
    print(country_top.head(top_n))
    return country_top.head(top_n)
top_country(df, top_n=5)

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

#sacar el df de las 10 canciones más populares

def popularity_characteristics(df, top_n=5):
    top_n_songs = top_songs(df, top_n=top_n)

    mean_danceability = top_n_songs["danceability"].mean()
    mean_energy = top_n_songs["energy"].mean()
    mean_valence = top_n_songs["valence"].mean()
    
    popularity_factors = {
        "danceability": mean_danceability,
        "energy": mean_energy,
        "valence": mean_valence
    }

    factor_mas_importante = max(popularity_factors, key=popularity_factors.get)

    print(f"Average characteristics in top {top_n} songs: {mean_danceability:.2f} danceability, {mean_energy:.2f} energy and {mean_valence:.2f} valence")
    print(f"So, the maximum value is: {popularity_factors[factor_mas_importante]:.2f} for {factor_mas_importante}")
popularity_characteristics(df, top_n=5)

#Cual es la cancion mas bailable?
def most_danceable_song(df):
    danceable_song = df.groupby("song_title")[("danceability")].mean()
    danceable_song = danceable_song.sort_values(ascending=False)
    print(f"Most danceable song: {danceable_song.index[0]}, with {danceable_song.iloc[0]:.2f} danceability")
most_danceable_song(df)

def most_energic_song(df):
    energic_song = df.groupby("song_title")[("energy")].mean()
    energic_song = energic_song.sort_values(ascending=False)
    print(f"Most energic song: {energic_song.index[0]}, with {energic_song.iloc[0]:.2f} energy")
most_energic_song(df)

def most_positive_song(df):
    positive_song = df.groupby("song_title")[("valence")].mean()
    positive_song = positive_song.sort_values(ascending=False)
    print(f"Most positive song: {positive_song.index[0]}, with {positive_song.iloc[0]:.2f} valence")
most_positive_song(df)

def prom_artist (df):
    artist_prom = df.groupby("artist")[("streams")].mean()
    artist_prom = artist_prom.sort_values(ascending=False)
    print(f"Artist with highest average streams: {artist_prom.index[0]}, with {artist_prom.iloc[0]:.2f} average streams")
prom_artist(df)

def duration_prom(df): 
    duration_prom = df.groupby("streams")[("duration_sec")].mean()
    duration_prom = duration_prom.sort_values(ascending=False)
    print(f"Duration with highest average streams: {duration_prom.index[0]}, with {duration_prom.iloc[0]:.2f} average duration in seconds")
    print(f"So, the duration in minutes is: {duration_prom.iloc[0]/60:.2f} minutes")
duration_prom(df)