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
    # Filtrar el DataFrame por el idioma dado
    peliculas_filtradas = df[df['original_language'].apply(
        lambda x: pd.notna(x) and Idioma in x)]
    # Obtener una lista de los nombres de las películas filtradas
    # nombres_peliculas = peliculas_filtradas['original_language'].count()
    nombres_peliculas = len(peliculas_filtradas)
    return {"Cantidad de peliculas: ": nombres_peliculas}
# print(buscar_peliculas_por_idioma('en'))


@app.get("/getPeliculasDuracion/{pelicula}")
def peliculas_duracion(Pelicula):
    # Filtrar el DataFrame por el nombre de la película
    filtro = df['title'] == Pelicula
    resultado = df.loc[filtro, ['release_date', 'runtime']]
    # Obtener el año de estreno y la duración
    año_estreno = resultado['release_date'].values[0].split('-')[0]
    duracion = resultado['runtime'].values[0]
    # Retornar el año de estreno y la duración como diccionario
    return {'año_estreno': año_estreno, 'duracion': duracion}


@app.get("/getFranquicia/{franquicia}")
def franquicia(Franquicia):
    # Filtrar el DataFrame por la franquicia dada
    peliculas_franquicia = df[df['belongs_to_collection'] == Franquicia]
    # Calcular el número de películas
    num_peliculas = len(peliculas_franquicia)
    # Calcular el monto total de revenue
    monto_total_revenue = peliculas_franquicia['revenue'].sum()
    # Calcular el promedio de revenue
    promedio_revenue = peliculas_franquicia['revenue'].mean()
    # Retornar las estadísticas como un diccionario
    return {'numero_peliculas': num_peliculas, 'monto_total_revenue': monto_total_revenue, 'promedio_revenue': promedio_revenue}


@app.get("/getPeliculasPais/{pais}")
def peliculas_pais(Pais):
    # Filtrar el DataFrame por el país dado, excluyendo valores NaN
    peliculas_pais = df[df['production_countries'].apply(
        lambda x: pd.notna(x) and Pais in x)]
    # Contar la cantidad de películas
    cantidad_peliculas = len(peliculas_pais)
    return cantidad_peliculas


@app.get("/getProductorasExitosas/{productora}")
def productoras_exitosas(Productora):
    # Filtrar el DataFrame por la productora dada
    peliculas_productora = df[df['production_companies'].apply(
        lambda x: pd.notna(x) and Productora in x)]
    # Contar el número de películas
    num_peliculas = len(peliculas_productora)
    # Calcular el revenue total
    revenue_total = peliculas_productora['revenue'].sum()
    return {'numero_peliculas': num_peliculas, 'revenue_total': revenue_total}


@app.get("/getDirector/{director}")
def get_director(nombre_director):
    peliculas_director = df[df['director'].apply(
        lambda x: pd.notna(x) and nombre_director in x)]
    # Calcular la suma de returns
    suma_returns = peliculas_director['return'].sum()
    # Obtener la lista de películas y sus detalles
    peliculas = peliculas_director[[
        'title', 'release_date', 'return', 'budget', 'revenue']].values.tolist()
    return {'suma_returns': suma_returns, 'lista_datos_peliculas': peliculas}


@app.get("/getRecomendacion/{titulo}")
def recomendacion(titulo):
    k=5
    movie_index = df[df['title'] == titulo].index[0]
    _, indices = knn_model.kneighbors(feature_matrix[movie_index], n_neighbors=k+1)
    recommended_movies = df.iloc[indices[0][1:]]['title'].tolist()
    return recommended_movies