from Backend.Data_motivation import connection_database_motivation, add_information_motivation, \
    get_information_motivation, show_results_motivation
from Frontend.Motivation_criteria import MotivationCriteria
from Frontend.Motivation_manager import MotivationManager
from Frontend.Performance_monitoring import PerformanceMonitoring
from Frontend.User import User
from Frontend.User_manager import UserManager

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

def main():
    #add_information_login_password('Boris', 'Casio2006')
    #add_information_users(get_id_login_password('Boris')[0], 'Boris', 'borisgostev29@mail.ru', 'manager', '1000000')
    #print(get_information_users(get_id_login_password('Boris')[0]))
    #add_information_motivation(get_id_login_password('Boris')[0], '1000', '10', '2', '12.01.2024', '12.02.2024')
    #show_results_motivation(get_information_motivation(get_id_login_password('Boris')[0]))
    #add_information_sales(get_id_login_password('Boris')[0], 100, '11.30.2024', '001', '2')
    #add_information_sales(get_id_login_password('Boris')[0], 100, '11.01.2024', '001', '3')
    #show_results_sales(get_information_sales(get_id_login_password('Boris')[0], '11.01.2024'))
    add_information_result_rewards(get_id_login_password('Boris')[0], '1000', '10.01.2024', '01.01.2025')
    #(get_information_sales_volume(get_id_login_password('Boris')[0], '10.01.2024', '01.01.2025')


if __name__ == "__main__":
    main()