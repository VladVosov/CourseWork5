import json


class Saving:
    """Класс для добавления информации сайта HH.ru в json-файл, его сортировки и удаления"""

    def __init__(self, data):
        self.company_id = None
        self.data = data
        self.filename = 'work.json'

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
                salary_to = i['salary']['to']
                requirement = i['snippet']['requirement']
                file = (self.company_id, name, url, salary_from, salary_to, requirement)
                list_file.append(file)

            return list_file

    def del_vacancy(self):
        """Чистим следы"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            pass