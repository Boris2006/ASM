import psycopg2

from Backend.Data_users import connection_database_users



def connection_database_sales(): #worked
    try:
        # Замените эти параметры на ваши данные подключения
        connection = psycopg2.connect(
            dbname="ASM",
            user="borisgostev",
            password="",
            host="localhost",
            port="5432"
        )

        #print("Соединение успешно установлено")
        return connection
    except Exception as e:
        #print("Ошибка при подключении к базе данных:", e)
        return False


def get_information_sales(user_id, start_date, end_date):
    connection = connection_database_users()
    try:
        cursor = connection.cursor()
        query = """
        SELECT * FROM sales
        WHERE id = %s AND date BETWEEN %s AND %s
        """
        cursor.execute(query, (user_id, start_date, end_date))
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка при получении информации о продажах: {e}")
        return []
    finally:
        connection.close()


def add_information_sales(user_id, amount, date, product_id, quantity):
    connection = connection_database_users()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO sales (id, amount, date, id_product, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, amount, date, product_id, 'completed'))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка при добавлении информации о продаже: {e}")
        connection.rollback()
        return False
    finally:
        connection.close()


def show_results_sales(sales): #worked
    for sale in sales:
        print(f"ID: {sale[0]}, Amount: {sale[1]}, Date: {sale[2]}, Id_product: {sale[3]}, Status: {sale[4]}")
