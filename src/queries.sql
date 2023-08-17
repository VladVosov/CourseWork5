#Создаем таблицу companies и добавляем в нее компании и employer_id

CREATE TABLE companies
(
	company_id serial PRIMARY KEY,
	company_name varchar NOT NULL,
	company_api int NOT NULL
)
INSERT INTO companies VALUES (1, 'Tinkoff', 78638)
INSERT INTO companies VALUES (2, 'Сбербанк-Сервис', 1473866)
INSERT INTO companies VALUES (3, 'Банк ВТБ', 4181)
INSERT INTO companies VALUES (4, 'Альфа-Банк', 80)
INSERT INTO companies VALUES (5, 'Ай-Теко (I-Teco)', 115)
INSERT INTO companies VALUES (6, 'КРОК', 2987)
INSERT INTO companies VALUES (7, 'Лаболатория Касперского', 1057)
INSERT INTO companies VALUES (8, 'Ланит Омни', 9251203)
INSERT INTO companies VALUES (9, 'IBS', 139)
INSERT INTO companies VALUES (10, 'VK', 15478)
SELECT * FROM companies


CREATE TABLE vacansies
(
	vacansy_id serial PRIMARY KEY,
	company_id serial,
	vacansy_name VARCHAR NOT NULL,
	vacansy_url VARCHAR NOT NULL,
	salary_from integer,
	salary_to integer,
	requirement text
)