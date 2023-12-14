import sys
sys.path.append("D:/bd_labs/Lab4_test")
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Employee
from typing import List

class EmployeeDAO(GeneralDAO):
  
    _domain_type = Employee

