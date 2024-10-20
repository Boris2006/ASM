import psycopg2
from Backend.Authentication_users import connection_database_login_password


def connection_database_users(): #worked
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


def get_id_login_password(login): #worked
    connection = connection_database_login_password()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM login_password WHERE login = %s", (login,))
        users = cursor.fetchall()
        cursor.close()
        return users
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False


def add_information_users(id, name, email, role, salary): #worked
    connection = connection_database_users()
    try:
        # Создаем курсор
        cursor = connection.cursor()
        # SQL-запрос для вставки данных
        insert_query = """
        INSERT INTO users (id, name, email, role, salary)
        VALUES (%s, %s, %s, %s, %s);
        """
        # Выполняем запрос с передачей параметров
        cursor.execute(insert_query, (id, name, email, role, salary))
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

def get_information_users(id): #worked
    connection = connection_database_users()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s;", (id,))
        user = cursor.fetchall()
        cursor.close()
        return user
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False

def show_results_users(users): #worked
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Role: {user[3]}, Salary: {user[4]}")
