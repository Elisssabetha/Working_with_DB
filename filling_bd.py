from src.config import config
from src.utils import get_employers_data, get_vacancies_data, save_employers_to_db, save_vacancies_to_db

params = config()
list_employers = get_employers_data()
list_vacancies = get_vacancies_data()

# сохраняем в бд данные по работодателям
save_employers_to_db(list_employers, params)

# сохраняем в бд данные по вакансиям
save_vacancies_to_db(list_vacancies, params)