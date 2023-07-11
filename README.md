# Proyecto Henry PI No. 1


## Descripcion: 
Este es el proyecto numero 1 del Bootcamp de Henry, en este tomamos el rol de Data Science en una start-up que provee servicios de agregación de plataformas de streaming.

## Paso 1
El primer paso que tomamos es hacer la transformación de datos correspondiente, para esto creamos el archivo "transformaciones.ipynb" en donde se tiene que ejecutar paso a paso todas las instrucciones para crear un nuevo archivo ya limpio el cual usaremos para poder hacer las consultas y entrenar al modelo. De igual manera se agrego una nueva columna la cual contiene el o los nombres de los directores que trabajaron en cada pelicula, esto para el metodo el correcto funcionamiento del metodo 'director'

## Paso 2
El segundo paso fune crear el archivo main.py en el cual leemos el archivo df_limpio y en el cual se encuentran los siguientes metodos de consulta.

- peliculas_idioma( Idioma: str): En el que se ingresa un idioma y este devolvera la cantidad de peliculas producidas en ese idioma.

- peliculas_duracion( Pelicula: str): En el que se ingresa el titulo de una pelicula y este metodo retorna la duracion en minutos de la misma y el año en que fue estrenada

- franquicia( Franquicia: str): En este metodo ingresamos el nombre de una franquicia y nos devuelve la cantidad de peliculas que conforma la franquicia, la ganancia total y el promedio de ganancia obtenida por todas las peliculas

- peliculas_pais( Pais: str): En este metodo ingresamos el nombre de un pais y este nos retornara el numero de peliculas que fueron producidas en dicho pais.

- productoras_exitosas( Productora: str): En este metodo ingresaremos el nombre de una productora y el metodo nos devolvera las ganancias totales de la productora asi como la cantidad de peliculas que ha hecho.

- get_director( nombre_director): En este metodo se ingresa el nombre de un director y nos devolvera el exito que ha tenido este en base a la suma de la columna 'return'(En la cual se encuentra el numero de veces que la pelicula ha superado en ganancias su costo), una lista con los siguientes campos nombre de cada pelicula, la fecha de lanzamiento, el retorno individual, el costo y la ganancia de la misma

## Paso 3
En este paso se llevo a cabo el EDA en el cual al principio cargamos el archivo que limpiamos en el paso numero 1 y en que ejecutaremos paso a paso los comandos correspondientes para poder para poder visualizar el analisis.

## Paso 4
En este paso nos encargamos de crear el modelo para hacer el metodo de recomendación el cual nos sugerira cinco peliculas en base al nombre de la pelicula que busquemos y el genero al que pertenece. Para hacer este metodo utilizamos el Modelo de K-Vecinos, ya que es un modelo adecuado para relaizar sistemas de recomendación. Entonces dentro del archivo que creamos en el paso dos llamado 'main.py' esribimos el codigo para entrenar el modelo y creamos el siguiente metodo:
- getRecomendacion: El cual se encarga de dat 5 recomendaciones de peliculas en base a la pelicula introducida, para este metodo se tomo como parametro para dar la recomendacion el titulo de la pelicula y su genero.


Estos son los enlaces en los que se puede ver el material creado para la correcta vizualizacion de este proyecto

- Enlace del Deploy en Render: https://proyecto-mlops-ajn4.onrender.com/docs

- Video en Youtube donde se explica todo el proyecto: https://youtu.be/Et24K-bFrnw

NOTA: En el siguiente link se ponen los archivos credtis.csv y movies_dataset.csv los cual deberan ser descargados y puestos en la carpeta Dataset:
https://drive.google.com/drive/folders/1NPj1FQTvDx0vY42gCOqDYbKyOkGWLqRb