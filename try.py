import duckdb
import pandas as pd

# Reemplaza '/ruta/a/mi_base_de_datos.duckdb' con la ruta correcta al archivo de tu base de datos
path_to_db = 'database.duckdb'

# Conectarse a la base de datos DuckDB
con = duckdb.connect(database=path_to_db)

# Realizar una consulta y cargar los resultados en un DataFrame de Pandas
query = "SELECT * FROM flights"  # Asegúrate de cambiar 'mi_tabla' por el nombre real de tu tabla
df = con.execute(query).df()

print(df)