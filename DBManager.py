import psycopg2


class DBManager:

    def get_companies_and_vacancies_count(self):

        """Получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self):

        """Получает список всех вакансий (название вакансии, название компании, зп, ссылка)"""
        pass

    def get_avg_salary(self):

        """Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):

        """Получает список всех вакансий, у которых зп выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self, keyword: str):

        """Получает список всех вакансий, в названии которых содержится ключевое слово"""
        pass



