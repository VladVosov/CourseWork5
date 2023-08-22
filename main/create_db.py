import psycopg2
import json
import main

# Подключаемся к базе данных (Введите свой хост, название БД, логин и пароль)
with psycopg2.connect(
        host="localhost",
        database="CourseWork5",
        user="postgres",
        password="123456"
) as conn:
    # Создаем курсор для работы с БД
    with conn.cursor() as cur:

        # Выполняем запрос на создание таблицы companies
        cur.execute("CREATE TABLE companies "
                    "(company_id serial PRIMARY KEY, "
                    "company_name varchar NOT NULL, "
                    "company_api int NOT NULL)")

        # Выполняем запрос на создание таблицы vacansies
        cur.execute("CREATE TABLE vacansies "
                    "(company_id serial, "
                    "vacansy_name VARCHAR NOT NULL, "
                    "vacansy_url VARCHAR NOT NULL, "
                    "salary_from integer, "
                    "requirement text, "
                    "vacansy_id serial PRIMARY KEY)")

        # Добавляем значения из файла data.json в таблицу companies
        with open('data.json', 'r') as f:
            date = json.load(f)

        for i in date:
            cur.execute("INSERT INTO companies VALUES (%s, %s, %s)", (i[0], i[1], i[2]))

        # Добавляем значения в таблицу vacansies
        with open('data.json', 'r') as f:
            date = json.load(f)

        for i in date:
            vacansies = main.hh.get_data("", i[2], i[0])

            for vac in vacansies:
                cur.execute("INSERT INTO vacansies VALUES (%s, %s, %s, %s, %s)",
                            (vac[0], vac[1], vac[2], vac[3], vac[4]))

# Закрываем курсор и подключение
conn.close()
