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
from Backend.Data_users import connection_database_users, get_id_login_password
from Backend.Data_users import get_information_users
from Backend.Data_users import add_information_users
from Backend.Data_users import show_results_users
from Backend.Report_generator import ReportGenerator

def main():
    #add_information_login_password('Boris', 'Casio2006')
    add_information_users(get_id_login_password('Boris')[0], 'Boris', 'borisgostev29@mail.ru', 'manager', '1000000')
    print(get_information_users(get_id_login_password('Boris')[0]))
if __name__ == "__main__":
    main()