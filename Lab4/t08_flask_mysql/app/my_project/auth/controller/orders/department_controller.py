from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import department_service
from t08_flask_mysql.app.my_project.auth.domain.orders.department import Department
from flask import abort
from http import HTTPStatus
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class DepartmentController(GeneralController):

    _service = department_service
