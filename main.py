from Frontend.Motivation_criteria import MotivationCriteria
from Frontend.Motivation_manager import MotivationManager
from Frontend.Performance_monitoring import PerformanceMonitoring
from Frontend.User import User
from Frontend.User_manager import UserManager

from Backend.Data_collector import SalesDataCollector
from Backend.Authentication_users import connection_database_login_password 
from Backend.Authentication_users import add_information_login_password 
from Backend.Authentication_users import get_information_login_password
from Backend.Authentication_users import verify_password
from Backend.Authentication_users import protected
from Backend.Data_motivation import connection_database_users
from Backend.Data_motivation import get_information_users
from Backend.Data_motivation import add_information_users
from Backend.Data_motivation import show_results_users
from Backend.Data_result_rewards import connection_database_result_rewards
from Backend.Data_result_rewards import get_information_sales_volume
from Backend.Data_result_rewards import get_information_result_rewards
from Backend.Data_result_rewards import add_information_result_rewards
from Backend.Data_result_rewards import show_results
from Backend.Data_sales import connection_database_sales
from Backend.Data_sales import get_information_sales
from Backend.Data_sales import show_results_sales
from Backend.Data_users import connection_database_users
from Backend.Data_users import get_information_users
from Backend.Data_users import add_information_users
from Backend.Data_users import show_results_users
from Backend.Report_generator import ReportGenerator

# Основной интерфейс программы
def main():
    user_manager = UserManager()
    motivation_manager = MotivationManager()
    performance_monitoring = PerformanceMonitoring()
    
    logged_in_user = None

    while True:
        if logged_in_user is None:
            print("\n1. Вход в аккаунт")
            print("2. Регистрация нового пользователя")
            print("3. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                user = user_manager.authenticate_user(username, password)
                if user:
                    logged_in_user = user
                    print(f"Добро пожаловать, {logged_in_user.username} ({logged_in_user.role})!")
                else:
                    print("Неверное имя пользователя или пароль.")

            elif choice == "2":
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                role = input("Введите должность (менеджер/руководитель): ")
                email = input("Введите электронную почту: ")
                salary = float(input("Введите зарплату: "))
                
                registration_result = user_manager.register_user(username, password, role, email, salary)
                print(registration_result)

            elif choice == "3":
                print("Выход из программы.")
                break

            else:
                print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

        # Интерфейс для авторизованных пользователей
        else:
            print("\nМеню:")
            if logged_in_user.role == 'руководитель':
                print("1. Добавить критерии мотивации")
                print("2. Просмотреть производительность сотрудников")
                print("3. Добавить нового сотрудника")
                print("4. Выход")

                choice = input("Выберите действие: ")

                if choice == "1":
                    sales_volume = float(input("Введите объем продаж: "))
                    closed_deals = int(input("Введите количество закрытых сделок: "))
                    retention_level = float(input("Введите уровень удержания клиентов: "))
                    start_date = input("Введите дату начала (YYYY-MM-DD): ")
                    end_date = input("Введите дату окончания (YYYY-MM-DD): ")
                    motivation_manager.add_criteria(sales_volume, closed_deals, retention_level, start_date, end_date)
                    print("Критерии мотивации добавлены успешно.")

                elif choice == "2":
                    print("Данные о производительности сотрудников:")
                    for entry in performance_monitoring.performance_data:
                        print(entry)

                elif choice == "3":
                    username = input("Введите имя нового сотрудника: ")
                    password = input("Введите пароль для нового сотрудника: ")
                    role = 'менеджер'  # все новые сотрудники - менеджеры
                    email = input("Введите электронную почту: ")
                    salary = float(input("Введите зарплату: "))
                    
                    registration_result = user_manager.register_user(username, password, role, email, salary)
                    print(registration_result)

                elif choice == "4":
                    print("Выход из программы.")
                    break

                else:
                    print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

            elif logged_in_user.role == 'менеджер':
                print("1. Добавить данные о производительности")
                print("2. Выход")

                choice = input("Выберите действие: ")

                if choice == "1":
                    employee_id = input("Введите ID сотрудника: ")
                    amount = float(input("Введите сумму: "))
                    date = input("Введите дату (ГГГГ-ММ-ДД): ")
                    type_client = input("Введите тип клиента: ")
                    performance_monitoring.add_performance_data(employee_id, amount, date, type_client)
                    print("Данные о производительности добавлены успешно.")

                elif choice == "2":
                    print("Выход из программы.")
                    break

                else:
                    print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()