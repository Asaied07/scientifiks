# Se realizan importaciones de bibliotecas necesarias
import os
import sqlite3
import pandas as pd

# meto blog.db en una variable
blog = 'blog.db'

# Creo una funcion simple para establecer la conexion
def get_conn():
    return sqlite3.connect(blog)

# a partir de aqui, empiezo a crear mis funciones SQL usando
# la funcion de mas arriba, y con with se maneja recursos de manera eficiente y segura, 
# especialmente cuando se trabaja con archivos o conexiones que necesitan ser cerrados después de su uso
def create_blog():
    with get_conn() as con:
        cur = con.cursor()
# cur.execute ejecuta la consulta SQL directamente sobre la base de datos
        cur.execute('''
            create table if not exists blog(
                    id integer primary key autoincrement,
                    titulo text not null,
                    categoria text not null,
                    autor text not null,
                    historia text not null)''')
        cur.execute("select count(*) from blog")
        # se iguala el resultado a una variable
        res=cur.fetchone()
        # aqui inserta datos solo si res en 0 es igual a cero
        if res is not None:
            if res[0]==0:
                current_dir = os.path.dirname(__file__)
                csv_path = os.path.join(current_dir, "blog.csv")
                df = pd.read_csv(csv_path)
                columns_to_insert = ['id','titulo','categoria','autor','historia']
                df.to_sql('blog', con, if_exists='append', index=False)