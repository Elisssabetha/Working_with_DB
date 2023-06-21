import psycopg2
import requests


def get_employers_data() -> list:
    """Получаем с hh инфо по работодателям"""
    list_employers = []
    for i in range(30, 35):  # номера страниц выбраны рандомно
        params = {
            'area': 113,  # Поиск по России
            'page': i,
            'per_page': 100,  # максимум 100
            'only_with_vacancies': True,
        }
        response = requests.get('https://api.hh.ru/employers', params=params)
        employers_data = response.json()['items']

        for employer in employers_data:
            emp = {'employer_id': employer['id'],
                   'employer_name': employer['name'],
                   'url': employer['url']
                   }
            list_employers.append(emp)
    return list_employers


def get_vacancies_data() -> list:
    """Получаем инфо о вакансиях работодателей"""

    list_vacancies = []

    list_employers_id = []
    for item in get_employers_data():
        list_employers_id.append(item['employer_id'])

    for i in range(0, 20):
        params = {
            'area': 113,  # Поиск по России
            'page': i,
            'per_page': 100,  # максимум 100
            'employer_id': list_employers_id,
            'only_with_salary': True,  # только с зп
            'currency': 'RUR'
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        vacancies_data = response.json()['items']

        for vacancy in vacancies_data:
            vac = {'vacancy_id': vacancy['id'],
                   'vacancy_name': vacancy['name'],
                   'employer_id': vacancy['employer']['id'],
                   'salary_from': vacancy['salary']['from'],
                   'salary_to': vacancy['salary']['to'],
                   'region': vacancy['area']['name'],
                   'url': vacancy['url']
                   }
            list_vacancies.append(vac)
    return list_vacancies


def save_employers_to_db(list_employers: list, params: dict) -> None:
    conn = psycopg2.connect(database='hh_info', **params)
    with conn:
        with conn.cursor() as cur:
            for employer in list_employers:
                cur.execute('insert into employers values (%s, %s, %s)', (
                    employer['employer_id'],
                    employer['employer_name'],
                    employer['url']

                ))
    conn.close()


def save_vacancies_to_db(list_vacancies: list, params: dict) -> None:
    conn = psycopg2.connect(database='hh_info', **params)
    with conn:
        with conn.cursor() as cur:
            for vacancy in list_vacancies:
                cur.execute('insert into vacancies values (%s, %s, %s, %s, %s, %s, %s)', (
                    vacancy['vacancy_id'],
                    vacancy['vacancy_name'],
                    vacancy['employer_id'],
                    vacancy['salary_from'],
                    vacancy['salary_to'],
                    vacancy['region'],
                    vacancy['url']
                ))
    conn.close()
