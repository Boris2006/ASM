from Backend.Data_motivation import connection_database_motivation, add_information_motivation, \
    get_information_motivation, show_results_motivation
from Frontend.Motivation_criteria import MotivationCriteria
from Frontend.Motivation_manager import MotivationManager
from Frontend.Performance_monitoring import PerformanceMonitoring
from Frontend.User import User
from Frontend.User_manager import UserManager
from Frontend.Reward_criteria import reward_criteria

from Backend.Authentication_users import connection_database_login_password 
from Backend.Authentication_users import add_information_login_password 
from Backend.Authentication_users import get_information_login_password
from Backend.Authentication_users import verify_password

from Backend.Data_result_rewards import connection_database_result_rewards
from Backend.Data_result_rewards import get_information_sales_volume
from Backend.Data_result_rewards import get_information_result_rewards
from Backend.Data_result_rewards import add_information_result_rewards
from Backend.Data_result_rewards import show_results
from Backend.Data_sales import connection_database_sales, add_information_sales
from Backend.Data_sales import get_information_sales
from Backend.Data_sales import show_results_sales
from Backend.Data_users import connection_database_users, get_id_login_password
from Backend.Data_users import get_information_users
from Backend.Data_users import add_information_users
from Backend.Data_users import show_results_users
from Backend.Report_generator import ReportGenerator

class ConsoleInterface:
    def start(self):
        self.main_menu()

    def main_menu(self):
        while True:
            print("\nГлавное меню:")
            print("1. Вход в систему")
            print("2. Регистрация нового пользователя")
            print("3. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.register_new_user()
            elif choice == "3":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def login(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if verify_password(login, password):
            user_id = get_id_login_password(login)[0][0]
            user_info = get_information_users(user_id)[0]
            user_role = user_info[3]
            if user_role == 'manager':
                self.manager_menu(user_id)
            else:
                self.employee_menu(user_id)
        else:
            print("Неверный логин или пароль.")

    def register_new_user(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        name = input("Введите имя: ")
        email = input("Введите email: ")
        role = input("Введите должность (manager/employee): ")
        salary = input("Введите зарплату: ")

        if add_information_login_password(login, password):
            user_id = get_id_login_password(login)[0][0]
            if add_information_users(user_id, name, email, role, salary):
                print("Пользователь успешно зарегистрирован.")
            else:
                print("Ошибка при добавлении информации о пользователе.")
        else:
            print("Ошибка при регистрации пользователя.")

    def manager_menu(self, user_id):
        while True:
            print("\nМеню менеджера:")
            print("1. Изменить должность сотрудника")
            print("2. Зарегистрировать нового сотрудника")
            print("3. Рассчитать мотивационные выплаты")
            print("4. Получить отчет о мотивационных выплатах")
            print("5. Просмотреть рейтинг сотрудников")
            print("6. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.change_employee_role()
            elif choice == "2":
                self.register_new_user()
            elif choice == "3":
                self.calculate_motivation_payments()
            elif choice == "4":
                self.generate_motivation_report()
            elif choice == "5":
                self.show_employee_rating()
            elif choice == "6":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def employee_menu(self, user_id):
        while True:
            print("\nМеню сотрудника:")
            print("1. Добавить новую продажу")
            print("2. Просмотреть свои мотивационные выплаты")
            print("3. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_new_sale(user_id)
            elif choice == "2":
                self.view_motivation_payments(user_id)
            elif choice == "3":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def change_employee_role(self):
        login = input("Введите логин сотрудника: ")
        new_role = input("Введите новую должность (manager/employee): ")
        user_id = get_id_login_password(login)[0][0]
        user_info = get_information_users(user_id)[0]
        if add_information_users(user_id, user_info[1], user_info[2], new_role, user_info[4]):
            print("Должность успешно изменена.")
        else:
            print("Ошибка при изменении должности.")

    def calculate_motivation_payments(self):
        user_id = int(input("Введите ID сотрудника: "))
        start_date = input("Введите начальную дату (YYYY-MM-DD): ")
        end_date = input("Введите конечную дату (YYYY-MM-DD): ")
        reward_criteria(user_id, start_date, end_date)
        print("Мотивационные выплаты рассчитаны.")

    def generate_motivation_report(self):
        start_date = input("Введите начальную дату (YYYY-MM-DD): ")
        end_date = input("Введите конечную дату (YYYY-MM-DD): ")
        report = ReportGenerator.generate_report(start_date, end_date)
        print("Отчет о мотивационных выплатах:")
        print(report)

    def show_employee_rating(self):
        start_date = input("Введите начальную дату (YYYY-MM-DD): ")
        end_date = input("Введите конечную дату (YYYY-MM-DD): ")
        rating = PerformanceMonitoring.get_employee_rating(start_date, end_date)
        print("Рейтинг сотрудников:")
        for i, employee in enumerate(rating, 1):
            print(f"{i}. {employee['name']} - Продажи: {employee['sales']}, Выплаты: {employee['rewards']}")

    def add_new_sale(self, user_id):
        amount = float(input("Введите сумму продажи: "))
        date = input("Введите дату продажи (YYYY-MM-DD): ")
        product_id = input("Введите ID продукта: ")
        quantity = int(input("Введите количество: "))
        if add_information_sales(user_id, amount, date, product_id, quantity):
            print("Продажа успешно добавлена.")
        else:
            print("Ошибка при добавлении продажи.")

    def view_motivation_payments(self, user_id):
        start_date = input("Введите начальную дату (YYYY-MM-DD): ")
        end_date = input("Введите конечную дату (YYYY-MM-DD): ")
        payments = get_information_result_rewards(user_id, start_date, end_date)
        if payments:
            print("Ваши мотивационные выплаты:")
            for payment in payments:
                print(f"Дата: {payment[3]}, Сумма: {payment[2]}")
        else:
            print("Мотивационные выплаты не найдены.")
