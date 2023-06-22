from src.DBManager import DBManager
from src.config import config
from src.utils import employers_info, all_vacancies, vacancies_with_higher_salary, search_vacancies_by_keyword


def main():
    params = config()
    dbmanager = DBManager(params)

    print('Какую информацию неоходимо получить из БД?')
    print("""Возможные варианты:
1 - Список работодателей и количество их вакансий
2 - Список всех вакансий
3 - Средняя зарплата по всем вакансиям
4 - Список вакансий за зарплатой выше средней
5 - Найти вакансии по ключевому слову
    """)
    user_answer = input('Введите число: \n')
    if user_answer == '1':
        employers_info(dbmanager)
    elif user_answer == '2':
        all_vacancies(dbmanager)
    elif user_answer == '3':
        print(f'Средняя зарплата по вакансиям: {dbmanager.get_avg_salary()} рублей в месяц')
    elif user_answer == '4':
        vacancies_with_higher_salary(dbmanager)
    elif user_answer == '5':
        search_vacancies_by_keyword(dbmanager)
    else:
        print('Некорректный ввод')


if __name__ == '__main__':
    main()
