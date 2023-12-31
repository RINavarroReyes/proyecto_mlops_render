from fastapi import FastAPI
#from pydantic import BaseModel
# import typing as tp
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


df = pd.read_csv('Dataset/df_limpio.csv')

df['combined_features'] = df['title'] + ' ' + df['genres'].fillna('')
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['combined_features'])
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(feature_matrix)


app = FastAPI()

# http://127.0.0.1:8000


@app.get("/getPeliculasIdioma/{idioma}")
def peliculas_idioma(Idioma):
    peliculas_filtradas = df[df['original_language'].apply(
        lambda x: pd.notna(x) and Idioma in x)]
    # nombres_peliculas = peliculas_filtradas['original_language'].count()
    nombres_peliculas = len(peliculas_filtradas)
    return {"Cantidad de peliculas: ": nombres_peliculas}
# print(buscar_peliculas_por_idioma('en'))


@app.get("/getPeliculasDuracion/{pelicula}")
def peliculas_duracion(Pelicula):
    filtro = df['title'] == Pelicula
    resultado = df.loc[filtro, ['release_date', 'runtime']]
    año_estreno = resultado['release_date'].values[0].split('-')[0]
    duracion = resultado['runtime'].values[0]
    return {'año de estreno': año_estreno, 'duracion': duracion}


@app.get("/getFranquicia/{franquicia}")
def franquicia(Franquicia):
    peliculas_franquicia = df[df['belongs_to_collection'] == Franquicia]
    num_peliculas = len(peliculas_franquicia)
    monto_total_revenue = peliculas_franquicia['revenue'].sum()
    promedio_revenue = peliculas_franquicia['revenue'].mean()
    return {'numero de peliculas': num_peliculas, 'monto total de ganancia': monto_total_revenue, 'promedio de ganancia': promedio_revenue}


@app.get("/getPeliculasPais/{pais}")
def peliculas_pais(Pais):
    peliculas_pais = df[df['production_countries'].apply(
        lambda x: pd.notna(x) and Pais in x)]
    cantidad_peliculas = len(peliculas_pais)
    return {'cantidad de pelicuculas':cantidad_peliculas}


@app.get("/getProductorasExitosas/{productora}")
def productoras_exitosas(Productora):
    peliculas_productora = df[df['production_companies'].apply(
        lambda x: pd.notna(x) and Productora in x)]
    num_peliculas = len(peliculas_productora)
    revenue_total = peliculas_productora['revenue'].sum()
    return {'numerode peliculas': num_peliculas, 'ganancia total': revenue_total}


@app.get("/getDirector/{director}")
def get_director(nombre_director):
    peliculas_director = df[df['director'].apply(
        lambda x: pd.notna(x) and nombre_director in x)]
    suma_returns = peliculas_director['return'].sum()
    peliculas = peliculas_director[[
        'title', 'release_date', 'return', 'budget', 'revenue']].values.tolist()
    return {'suma de retorno': suma_returns, 'lista de datos de pelicula': peliculas}


@app.get("/getRecomendacion/{titulo}")
def recomendacion(titulo):
    k=5
    movie_index = df[df['title'] == titulo].index[0]
    _, indices = knn_model.kneighbors(feature_matrix[movie_index], n_neighbors=k+1)
    recommended_movies = df.iloc[indices[0][1:]]['title'].tolist()
    return {'Peliculas recomendadas': recommended_movies}