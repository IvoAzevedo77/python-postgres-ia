import psycopg2
import os

# Obtém as informações de conexão a partir das variáveis de ambiente
dbname = "db-ia"
user = os.getenv("USER")
password = os.getenv("PRIVATEKEYPOSTGRES")
host = "database-ea.cvkei0o2ei4o.eu-central-1.rds.amazonaws.com"
port = "5432"

# Conecta-se ao banco de dados
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Executa a consulta
cursor.execute('SELECT * FROM public.contacts;')

# Recupera os resultados
results = cursor.fetchall()

# Fecha o cursor e a conexão
cursor.close()
conn.close()

# Itera sobre os resultados e imprime-os
for x in results:
    print(x)