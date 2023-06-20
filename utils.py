import requests


def get_employers_data() -> list:

    """Получаем с hh инфо по работодателям"""

    params = {
        'area': 113,  # Поиск по России
        'page': 0,
        'per_page': 30,  # максимум 100
        'only_with_vacancies': True
    }
    response = requests.get('https://api.hh.ru/employers', params=params)
    employers_data = response.json()
    return employers_data['items']


def get_vacancies_data() -> list:

    """Получаем инфо о вакансиях работодателей"""

    list_employers_id = []
    for item in get_employers_data():
        list_employers_id.append(item['id'])

    params = {
        'area': 113,  # Поиск по России
        'page': 0,
        'per_page': 100,  # максимум 100
        'employer_id': list_employers_id,
        'only_with_salary': True  # только с зп
    }
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    vacancies_data = response.json()
    return vacancies_data['items']
