import psycopg2
import os
print(os.environ)


try:
    # Conecta ao banco de dados
    conn = psycopg2.connect(
        host='3.121.182.90',
        port=5432,
        database='db-ia',
        user='postgres',
        password='Abcd1234!'
    )

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Define a consulta SQL
    query = "SELECT * FROM public.contacts"

    # Executa a consulta
    cursor.execute(query)

    # Recupera todos os resultados da consulta
    results = cursor.fetchall()

    # Itera sobre os resultados e imprime cada linha
    for row in results:
        print(row)

    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")