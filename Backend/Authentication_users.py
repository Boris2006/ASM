import psycopg2
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

def connection_database_login_password():
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


def add_information_login_password(login, password):
    connection = connection_database_login_password()
    try:
        # Создаем курсор
        cursor = connection.cursor()
        # SQL-запрос для вставки данных
        insert_query = """
        INSERT INTO login_password (login, password)
        VALUES (%s, %s);
        """
        # Выполняем запрос с передачей параметров
        cursor.execute(insert_query, (login, password))
        # Зафиксировать изменения в базе данных
        connection.commit()
        # Закрываем курсор
        cursor.close()
        return True #i can change code
    except Exception as e:
        connection.rollback()  # Откат изменений в случае ошибки
        return False


def get_information_login_password(login):
    connection = connection_database_login_password()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM login_password WHERE login = %s;", (login,))
        user = cursor.fetchall()
        cursor.close()
        return user
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")


@auth.verify_password
def verify_password(login, password):
    login_password = get_information_login_password(login)
    for l_p in login_password:
        if login == l_p[1] and l_p[2] == password:
            return login

if __name__ == '__main__':
    app.run(debug=True)