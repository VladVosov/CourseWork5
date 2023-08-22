import requests
import json


class GD_on_API:
    """Класс для работы с API сайта с вакансиями HH.ru"""
    def __init__(self, keyword, employer_id, page=0):
        self.url = 'https://api.hh.ru/vacancies'
        self.employer_id = employer_id
        self.params = {"text": keyword, "page": page, "employer_id": employer_id, "only_with_salary": True}

    def get_request(self):
        """На основе ссылки, страницы сайта и пользовательского запроса получаем данные сайта hh.ru"""
        return requests.get(self.url, params=self.params)


class Saving:
    """Класс для добавления информации сайта HH.ru в json-файл, его сортировки и удаления"""

    def __init__(self, data):
        self.company_id = None
        self.data = data
        self.filename = 'hh.json'

    def add_vacancy(self):
        """Сохраняем информацию в json-файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, sort_keys=True, indent=4)

    def get_vacancy(self, company_id):
        """Сортируем информацию и достаем то, что нам нужно в список словарей"""
        self.company_id = company_id
        list_file = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            full_file = json.load(file)['items']
            for i in full_file:
                name = i['name']
                url = i['url']
                if i['salary'] is None:
                    continue
                if i['salary']['currency'] != 'RUR':
                    continue
                salary_from = i['salary']['from']
                if salary_from is None:
                    salary_from = 0
                requirement = i['snippet']['requirement']
                file = [self.company_id, name, url, salary_from, requirement]
                list_file.append(file)

            return list_file

    def del_vacancy(self):
        """Чистим следы"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            pass


def get_data(keyword, company_api, company_id):
    """Функция для вывода готового списка вакансий"""
    data = GD_on_API(keyword, company_api)
    data_get = data.get_request().json()
    data_add = Saving(data_get)
    data_add.add_vacancy()
    data_list = data_add.get_vacancy(company_id)
    data_add.del_vacancy()
    return data_list
