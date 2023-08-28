import psycopg2


class DBManager:
    """Класс для работы с БД"""
    def __init__(self, database, user, password):
        self.host = "localhost"
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        """Устанавливает соединение с БД"""
        self.connection = psycopg2.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        """Разрывает соединение с БД"""
        self.cursor.close()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        self.cursor.execute("SELECT name, open_vacancies FROM employers")
        rows = self.cursor.fetchall()
        n = 1

        for row in rows:
            print(f"{n} | name: {row[0]} | open vacancies: {row[1]}")
            n += 1

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию"""
        self.cursor.execute("SELECT employers.name, vacancies.name, salary, vacancies.url FROM vacancies JOIN employers USING(employer_id)")
        rows = self.cursor.fetchall()
        n = 1

        for row in rows:
            print(f"{n} | employer name: {row[0]} | vacancy name: {row[1]} | salary: {row[2]} | vacancy url: {row[3]}")
            n += 1

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        self.cursor.execute("SELECT AVG(salary) FROM vacancies")

        print(f"average salary: {float(self.cursor.fetchone()[0])}")

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.cursor.execute("SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)")
        rows = self.cursor.fetchall()
        n = 1

        for row in rows:
            print(f"{n} | vacancy id: {row[0]} | employer id: {row[1]} | vacancy name: {row[2]} | published at: {row[3]} | salary: {row[4]} | vacancy url: {row[5]} | description: {row[6]}")
            n += 1

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        self.cursor.execute(f"SELECT * FROM vacancies WHERE name LIKE '%{keyword}%'")
        rows = self.cursor.fetchall()
        n = 1

        for row in rows:
            print(f"{n} | vacancy id: {row[0]} | employer id: {row[1]} | vacancy name: {row[2]} | published at: {row[3]} | salary: {row[4]} | vacancy url: {row[5]} | description: {row[6]}")
            n += 1
