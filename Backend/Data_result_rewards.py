import psycopg2

def connection_database_users():
    try:
        # Замените эти параметры на ваши данные подключения
        connection = psycopg2.connect(
            dbname="result_rewards",
            user="borisgostev",
            password="",
            host="localhost",
            port="5432"
        )

        print("Соединение успешно установлено")
        return connection
    except Exception as e:
        print("Ошибка при подключении к базе данных:", e)


def get_information_sales_volume(connection, id, start_date, end_date):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sales WHERE date BETWEEN %s AND %s, id = %s", (start_date, end_date, id))
        total_sales = cursor.fetchall()
        cursor.close()
        return total_sales
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

def get_information_result_rewards(connection, start_date, end_date):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM result_rewards WHERE date BETWEEN %s AND %s, id = %s", (start_date, end_date, id))
        bonuses = cursor.fetchall()
        cursor.close()
        return bonuses
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

def add_information_result_rewards(connection, id, total_sales, motivation_bonus, base_salary, start_date, end_date):
        try:
            # Создаем курсор
            cursor = connection.cursor()
            # SQL-запрос для вставки данных
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
