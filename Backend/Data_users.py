import psycopg2

def connection_database_users():
    try:
        # Замените эти параметры на ваши данные подключения
        connection = psycopg2.connect(
            dbname="users",
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
        cursor.execute("SELECT * FROM login_password WHERE id = %s", (id))
        users = cursor.fetchall()
        cursor.close()
        return users
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")


def add_information_users(connection, name, email, role, salary):
        try:
            # Создаем курсор
            cursor = connection.cursor()
            # SQL-запрос для вставки данных
            insert_query = """
            INSERT INTO users (name, email, role, salary)
            VALUES (%s, %s, %s, %s);
            """
            # Выполняем запрос с передачей параметров
            cursor.execute(insert_query, (name, email, role, salary))
            # Зафиксировать изменения в базе данных
            connection.commit()
            # Закрываем курсор
            cursor.close()
            print("Запись успешно добавлена.")
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            connection.rollback()  # Откат изменений в случае ошибки


def show_results_users(users):
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Role: {user[3]}, Salary: {user[4]}")
