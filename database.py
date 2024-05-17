import psycopg2
import os
import sys

# Obtém as informações de conexão a partir das variáveis de ambiente
dbname = "db-ia"
user = os.getenv("USER")
password = os.getenv("PRIVATEKEYPOSTGRES")
host = "database-ea.cvkei0o2ei4o.eu-central-1.rds.amazonaws.com"
port = "5432"

# Verifica se as variáveis de ambiente estão definidas corretamente
if not user:
    print("A variável de ambiente USER não está definida.")
    sys.exit(1)
if not password:
    print("A variável de ambiente PRIVATEKEYPOSTGRES não está definida.")
    sys.exit(1)

try:
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

    # Itera sobre os resultados e imprime-os
    for x in results:
        print(x)

except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)

finally:
    # Fecha o cursor e a conexão
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()