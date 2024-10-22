import psycopg2

from Backend.Data_users import connection_database_users

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

def add_information_motivation(sales_volume, closed_deals, retention_level, start_date, end_date):
    connection = connection_database_users()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO motivation_criteria (sales_volume, closed_deals, retention_level, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (sales_volume, closed_deals, retention_level, start_date, end_date))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка при добавлении информации о критериях мотивации: {e}")
        connection.rollback()
        return False
    finally:
        connection.close()

def get_information_motivation(start_date, end_date):
    connection = connection_database_users()
    try:
        cursor = connection.cursor()
        query = """
        SELECT * FROM motivation_criteria
        WHERE start_date <= %s AND end_date >= %s
        ORDER BY id DESC LIMIT 1
        """
        cursor.execute(query, (start_date, end_date))
        return cursor.fetchone()
    except Exception as e:
        print(f"Ошибка при получении информации о критериях мотивации: {e}")
        return None
    finally:
        connection.close()

def show_results_motivation(users): #worked
    for user in users:
        print(f"ID: {user[0]}, Sales_volume: {user[1]}, Closed_deals: {user[2]}, Retention_level: {user[3]}, Start_date: {user[4]}, End_date: {user[5]}")
