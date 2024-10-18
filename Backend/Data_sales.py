import psycopg2

def connection_database_sales():
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


def get_information_sales(connection, id, date):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sales WHERE id = %s, date = %s", (id, date))
        sales = cursor.fetchall()
        cursor.close()
        return sales
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")


def add_information_sales(connection, id, amount, date, id_sale, status):
        try:
            # Создаем курсор
            cursor = connection.cursor()
            # SQL-запрос для вставки данных
            insert_query = """
            INSERT INTO sales (id, amount, date, id_sale, status)
            VALUES (%s, %s, %s, %s, %s);
            """
            # Выполняем запрос с передачей параметров
            cursor.execute(insert_query, (id, amount, date, id_sale, status))
            # Зафиксировать изменения в базе данных
            connection.commit()
            # Закрываем курсор
            cursor.close()
            print("Запись успешно добавлена.")
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            connection.rollback()  # Откат изменений в случае ошибки


def show_results_sales(sales):
    for sale in sales:
        print(f"ID: {sale[0]}, Amount: {sale[1]}, Date: {sale[2]}, Id_sale: {sale[3]}, Status: {sale[4]}")
