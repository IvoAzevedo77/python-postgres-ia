import psycopg2
import os
import sys
#print(os.environ)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])


conn = psycopg2.connect(
    dbname="db-ia",
    user="postgres",
    password="Abcd1234!",
    host="database-ea.cvkei0o2ei4o.eu-central-1.rds.amazonaws.com",
    port="5432"
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM public.contacts;')
results = cursor.fetchall()
conn.close()

for x in results:
    print(x)
