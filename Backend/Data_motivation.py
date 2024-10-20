import psycopg2

def connection_database_motivation(): #worked
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

def add_information_motivation(id, sales_volume, closed_deals, retention_level, start_date, end_date): #worked
    connection = connection_database_motivation()
    try:
        # Создаем курсор
        cursor = connection.cursor()
        # SQL-запрос для вставки данных
        insert_query = """
        INSERT INTO motivation_criteria (id, sales_volume, closed_deals, retention_level, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        # Выполняем запрос с передачей параметров
        cursor.execute(insert_query, (id, sales_volume, closed_deals, retention_level, start_date, end_date,))
        # Зафиксировать изменения в базе данных
        connection.commit()
        # Закрываем курсор
        cursor.close()
        print("Запись успешно добавлена.")
        return True
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        connection.rollback()  # Откат изменений в случае ошибки
        return False

def get_information_motivation(id): #worked
    connection = connection_database_motivation()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM motivation_criteria WHERE id = %s", (id,))
        user = cursor.fetchall()
        cursor.close()
        return user
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False

def show_results_motivation(users): #worked
    for user in users:
        print(f"ID: {user[0]}, Sales_volume: {user[1]}, Closed_deals: {user[2]}, Retention_level: {user[3]}, Start_date: {user[4]}, End_date: {user[5]}")
