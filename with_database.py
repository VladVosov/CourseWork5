import psycopg2

# Подключаемся к базе данных (Введите свой хост, название БД, логин и пароль)
with psycopg2.connect(
        host="localhost",
        database="Course_Work_5",
        user="postgres",
        password="123456"
) as conn:
    # Создаем курсор для работы с БД
    with conn.cursor() as cur:
        # Выполняем запрос на чтение таблицы companies
        cur.execute("SELECT * FROM companies")

        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[2])

# Закрываем курсор и подключение
conn.close()
