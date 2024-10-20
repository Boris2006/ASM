import psycopg2

from Backend.Data_sales import connection_database_sales
from Backend.Data_users import get_information_users


def connection_database_result_rewards():
    try:
        # Замените эти параметры на ваши данные подключения
        connection = psycopg2.connect(
            dbname="ASM",
            user="borisgostev",
            password="",
            host="localhost",
            port="5432"
        )

        print("Соединение успешно установлено")
        return connection
    except Exception as e:
        print("Ошибка при подключении к базе данных:", e)
        return False


def get_information_sales_volume(id, start_date, end_date):
    connection = connection_database_sales()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT amount FROM sales WHERE id = %s AND date BETWEEN %s AND %s", (id, start_date, end_date,))
        total_sales = cursor.fetchall()
        cursor.close()
        volume = 0
        for sale in total_sales:
            volume = volume + int(sale[0])
        return volume
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False

def get_information_result_rewards(id, start_date, end_date):
    connection = connection_database_result_rewards()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM result_rewards WHERE date BETWEEN %s AND %s AND id = %s", (start_date, end_date, id))
        bonuses = cursor.fetchall()
        cursor.close()
        return bonuses
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

def add_information_result_rewards(id, motivation_bonus, start_date, end_date):
    connection = connection_database_result_rewards()
    try:
        # Создаем курсор
        cursor = connection.cursor()
        # SQL-запрос для вставки данных
        total_sales = get_information_sales_volume(id, start_date, end_date)
        sales = get_information_users(id)
        for sal in sales:
            base_salary = sal[4]
        insert_query = """
        INSERT INTO result_rewards (id, total_sales, motivation_bonus, base_salary, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        # Выполняем запрос с передачей параметров
        cursor.execute(insert_query, (id, total_sales, motivation_bonus, base_salary, start_date, end_date))
        # Зафиксировать изменения в базе данных
        connection.commit()
        # Закрываем курсор
        cursor.close()
        print("Запись успешно добавлена.")
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        connection.rollback()  # Откат изменений в случае ошибки


def show_results(bonuses):
    for bonus in bonuses:
        print(f"ID: {bonus[0]}, Total_sales: {bonus[1]}, Motivation_bonus: {bonus[2]}, Base_salary: {bonus[3]}, Start_date: {bonus[4]}, End_date: {bonus[5]}")
