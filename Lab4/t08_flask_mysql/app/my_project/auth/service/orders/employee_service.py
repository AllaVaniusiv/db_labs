from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import employee_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.employee import Employee
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class EmployeeService(GeneralService):

    _dao = employee_dao
