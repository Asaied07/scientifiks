# Desde: se crea la imagen para el contenedor a partir de la imagen python:alpine
FROM python:alpine

# Se establece un directorio de trabajo, en este caso /src
WORKDIR /src

# se copia el contenido de ./src (que debe estar en el mismo nivel del dockerfile)
# en la carpeta declarada como directorio de trabajo
COPY ./src .

# instala las dependencias descritas en el archivo requirements.txt
# la opcion -r lee desde un archivo
RUN pip install --no-cache-dir -r requirements.txt

# la instruccion CMD declara un comando que se ejecutara a partir de que 
# la imagen sea usada para un contenedor, con lo cual se ejecutara
# el principal ejecutable que se encarga de llamar a todos los demas
CMD ["python3", "run.py"]