"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

from config import PSWD

with psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password=PSWD,
) as conn:
    with conn.cursor() as cur:
        with open('north_data\\customers_data.csv', 'r') as file:
            header = next(file)
            reader = csv.reader(file)
            for row in reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        with open('north_data\\employees_data.csv', 'r') as file:
            header = next(file)
            reader = csv.reader(file)
            for row in reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        with open('north_data\\orders_data.csv', 'r') as file:
            header = next(file)
            reader = csv.reader(file)
            for row in reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

conn.close()
