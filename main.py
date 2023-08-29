import os
from DBManager import DBManager
from create_tables import create_db, create_and_fill_tables


create_db()
create_and_fill_tables()

dbm = DBManager("coursework_5", "postgres", os.getenv('PG_PASSWORD'))
dbm.connect()

print("""Вывести список всех компаний и количество вакансий у каждой компании - 1
Вывести список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию - 2
Вывести среднюю зарплату по вакансиям - 3
Вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям - 4
Вывести список всех вакансий, в названии которых содержится слово - 5\n""")

user_input = input()
if user_input == "1":
    dbm.get_companies_and_vacancies_count()
elif user_input == "2":
    dbm.get_all_vacancies()
elif user_input == "3":
    dbm.get_avg_salary()
elif user_input == "4":
    dbm.get_vacancies_with_higher_salary()
elif user_input == "5":
    user_keyword = input("Введите ключевое слово: ")
    dbm.get_vacancies_with_keyword(user_keyword)
else:
    print("Неверный ввод!")

dbm.disconnect()
