import pandas as pd
from sqlalchemy import create_engine

# Leer Excel
df = pd.read_excel(
    "C:\\Users\\allhs\\Documents\\Python_projects\\Music_charts\\Data\\music_charts_project_dataset.xlsx"
)


# Renombrar columnas para coincidir con MySQL
df = df.rename(columns={
    "rank": "rank_position"
})


# Conexión a MySQL
engine = create_engine(
    "mysql+pymysql://root:75537342@localhost/music_charts"
)


# Insertar datos
df.to_sql(
    "music_charts",
    con=engine,
    if_exists="append",
    index=False
)

print(f"{len(df)} filas importadas correctamente")
