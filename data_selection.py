from DBManager import DBManager


dbm = DBManager("coursework_5", "postgres", "cds543")
dbm.connect()

dbm.get_companies_and_vacancies_count()
# dbm.get_all_vacancies()
# dbm.get_avg_salary()
# dbm.get_vacancies_with_higher_salary()
# dbm.get_vacancies_with_keyword("менеджер")

dbm.disconnect()
