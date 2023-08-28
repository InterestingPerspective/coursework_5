from funcs_for_db import converted_employers, converted_vacancies
import psycopg2


# Скрипт, который заполняет таблицы данными
with psycopg2.connect(
    host="localhost",
    database="coursework_5",
    user="postgres",
    password="cds543"
) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO employers VALUES (%s, %s, %s, %s, %s, %s)", converted_employers())
        cur.executemany("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)", converted_vacancies())

conn.close()
