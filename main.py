import pandas as pd
#from Backend.Authentication_users import connection_database_login_password
from Backend.Authentication_users import add_information_login_password
from Backend.Authentication_users import get_information_login_password
from Backend.Authentication_users import verify_password

#add_information_login_password('Boris', 'Casio2006')
print(verify_password('Boris', 'Casio2006'))

