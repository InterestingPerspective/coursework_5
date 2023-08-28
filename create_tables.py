import psycopg2


# Скрипт, который создаёт 2 таблицы (работодателей и вакансии)
with psycopg2.connect(
    host="localhost",
    database="coursework_5",
    user="postgres",
    password="cds543"
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

conn.close()
