import psycopg2


class DBManager:

    def __init__(self, host, dbname, user, password):
        self.password = password
        self.user = user
        self.dbname = dbname
        self.host = host
        self.request = None

    def connect(self, request):
        """Подключаемся к базе данных, выполняем команду и закрываем БД"""
        self.request = request
        # Подключаемся к базе данных
        with psycopg2.connect(
                host=self.host,  # "localhost"
                database=self.dbname,  # "CourseWork5"
                user=self.user,  # "postgres"
                password=self.password  # "123456"
        ) as conn:
            # Создаем курсор для работы с БД
            with conn.cursor() as cur:
                # Выполняем запрос
                cur.execute(self.request)
                # Возвращаем данные
                rows = cur.fetchall()
                return rows

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию"""

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""


test = DBManager("localhost", "CourseWork5", "postgres", "123456")
print(test.connect('SELECT * FROM companies'))
