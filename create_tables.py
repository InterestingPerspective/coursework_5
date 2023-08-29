import os
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from funcs_for_db import converted_employers, converted_vacancies


def create_db():
    """Создаёт БД"""
    conn = connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=os.getenv('PG_PASSWORD'))

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE coursework_5")
    cur.close()
    conn.close()


def create_and_fill_tables():
    """Скрипт, который создаёт 2 таблицы (работодателей и вакансии) и заполняет их"""
    with connect(
        host="localhost",
        database="coursework_5",
        user="postgres",
        password=os.getenv('PG_PASSWORD')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE employers
                (employer_id int PRIMARY KEY,
                name varchar(100) NOT NULL,
                url varchar(100) NOT NULL,
                vacancies_url varchar(100) NOT NULL,
                open_vacancies int NOT NULL,
                description text);''')

            cur.execute('''CREATE TABLE vacancies
                (vacancy_id int PRIMARY KEY,
                employer_id int REFERENCES employers(employer_id) NOT NULL,
                name varchar(100) NOT NULL,
                published_at varchar(50) NOT NULL,
                salary int,
                url varchar(100) NOT NULL,
                description text);''')

            cur.executemany("INSERT INTO employers VALUES (%s, %s, %s, %s, %s, %s)", converted_employers())
            cur.executemany("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)", converted_vacancies())

    conn.close()
