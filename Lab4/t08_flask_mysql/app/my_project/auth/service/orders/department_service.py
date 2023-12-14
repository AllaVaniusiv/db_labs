from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import department_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.department import Department
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class DepartmentService(GeneralService):

    _dao = department_dao
