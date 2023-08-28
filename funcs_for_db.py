import requests


def get_employers():
    """Получает работодателей с открытыми вакансиями из сферы IT по API"""
    url = "https://api.hh.ru/employers"
    params = {"text": "IT", "per_page": 100, "sort_by": "by_vacancies_open"}
    response = requests.get(url, params=params)

    return response.json()["items"]


def get_employer_description(employer_id):
    """Получает описание работодателя по его ID"""
    url = f"https://api.hh.ru/employers/{employer_id}"
    response = requests.get(url)

    return response.json()["description"]


def choose_employers():
    """Выбирает 10 работодателей с кол-вом вакансий от 50 до 250"""
    employers = []

    for employer in get_employers():
        if 50 <= employer['open_vacancies'] <= 250 and len(employers) != 10:
            employers.append(employer)

    return employers


def converted_employers():
    """Конвертирует работодателей в список кортежей"""
    employers = []

    for employer in choose_employers():
        data = (int(employer['id']),
                employer['name'],
                employer['url'],
                employer['vacancies_url'],
                employer['open_vacancies'],
                get_employer_description(employer['id']))
        employers.append(data)

    return employers


def get_vacancies(vacancies_url):
    """Получает инфу о вакансии по ссылке"""
    response = requests.get(vacancies_url)

    return response.json()["items"]


def all_vacancies():
    """Добавляет все вакансии в список"""
    vacancies = []

    for employer in choose_employers():
        vacancies.append(get_vacancies(employer['vacancies_url']))

    return vacancies


def converted_vacancies():
    """Конвертирует вакансии в список кортежей"""
    conv_vacancies = []

    for vacancies in all_vacancies():
        for vacancy in vacancies:
            if vacancy['salary'] is None:
                data = (int(vacancy['id']),
                        vacancy['employer']['id'],
                        vacancy['name'],
                        vacancy['published_at'],
                        None,
                        vacancy['url'],
                        vacancy['snippet']['requirement'])
                conv_vacancies.append(data)
            else:
                data = (int(vacancy['id']),
                        vacancy['employer']['id'],
                        vacancy['name'],
                        vacancy['published_at'],
                        vacancy['salary']['from'],
                        vacancy['url'],
                        vacancy['snippet']['requirement'])
                conv_vacancies.append(data)

    return conv_vacancies
