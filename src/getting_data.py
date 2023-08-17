import requests


class GD_on_API:
    """Класс для работы с API сайта с вакансиями HH.ru"""
    def __init__(self, keyword, employer_id, page=0):
        self.url = 'https://api.hh.ru/vacancies'
        self.employer_id = employer_id
        self.params = {"text": keyword, "page": page, "employer_id": employer_id, "only_with_salary": True}

    def get_request(self):
        """На основе ссылки, страницы сайта и пользовательского запроса получаем данные сайта hh.ru"""
        return requests.get(self.url, params=self.params)


test = GD_on_API('', '78638')
print(test.get_request().json())