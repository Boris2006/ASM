import psycopg2

# Основная функция для вычисления и добавления наград
def reward_criteria(user_id, start_date, end_date):
    user_connection = connection_database_users()
    rewards_connection = connection_database_result_rewards()

    # Получаем информацию о пользователе
    user_info = get_information_users(user_connection, user_id)
    
    if not user_info:
        print("Пользователь не найден.")
        return

    user_data = user_info[0]
    sales_volume = user_data[1]
    closed_deals = user_data[2]
    retention_level = user_data[3]

    # Получаем информацию о продажах
    total_sales = get_information_sales_volume(rewards_connection, user_id, start_date, end_date)
    total_sales_value = sum(sale[1] for sale in total_sales)  # Предполагаем, что значение продаж на втором месте

    # Логика расчета мотивационного бонуса
    motivation_bonus = calculate_bonus(total_sales_value, sales_volume, closed_deals, retention_level)

    # Добавляем информацию о результатах наград
    base_salary = 50000  # Пример базовой зарплаты
    add_information_result_rewards(rewards_connection, user_id, total_sales_value, motivation_bonus, base_salary, start_date, end_date)

    # Закрываем соединения
    user_connection.close()
    rewards_connection.close()

# Функция для расчета мотивационного бонуса
def calculate_bonus(total_sales, sales_volume, closed_deals, retention_level):
    # Здесь можно использовать любую логику для расчета бонуса
    bonus = (total_sales / sales_volume) * (closed_deals / 10) * (retention_level / 100)
    return round(bonus, 2)

# Вызов функции награждения
if __name__ == "__main__":
    reward_criteria(user_id=1, start_date='2023-01-01', end_date='2023-12-31')