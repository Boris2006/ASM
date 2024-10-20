import psycopg2

def connection_database_users():
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


def get_information_users(connection, id):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM motivation_criteria WHERE id = %s", (id))
        user = cursor.fetchall()
        cursor.close()
        return user
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")


def add_information_users(connection, id, sales_volume, closed_deals, retention_level, start_date, end_date):
        try:
            # Создаем курсор
            cursor = connection.cursor()
            # SQL-запрос для вставки данных
            insert_query = """
            INSERT INTO motivation_criteria (id, sales_volume, closed_deals, retention_level, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            # Выполняем запрос с передачей параметров
            cursor.execute(insert_query, (id, sales_volume, closed_deals, retention_level, start_date, end_date))
            # Зафиксировать изменения в базе данных
            connection.commit()
            # Закрываем курсор
            cursor.close()
            print("Запись успешно добавлена.")
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            connection.rollback()  # Откат изменений в случае ошибки


def show_results_users(user):
    print(f"ID: {user[0]}, Sales_volume: {user[1]}, Closed_deals: {user[2]}, Retention_level: {user[3]}, Start_date: {user[4]}, End_date: {user[5]}")
