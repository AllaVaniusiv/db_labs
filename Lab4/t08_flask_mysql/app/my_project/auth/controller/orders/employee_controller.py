from http import HTTPStatus
from typing import List

from flask import abort
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.domain.orders.employee import Employee
from t08_flask_mysql.app.my_project.auth.service import employee_service
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class EmployeeController(GeneralController):

    _service = employee_service

