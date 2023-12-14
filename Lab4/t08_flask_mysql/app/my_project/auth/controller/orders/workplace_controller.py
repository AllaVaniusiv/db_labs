from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import workplace_service
from http import HTTPStatus
import sys
from typing import List

from flask import abort
from t08_flask_mysql.app.my_project.auth.domain.orders.workplace import Workplace
sys.path.append("D:/bd_labs/Lab4_test")


class WorkplaceController(GeneralController):

    _service = workplace_service

    def get_employees_in_workplace(self, workplace_id):
        return workplace_service.get_employees_in_workplace(workplace_id)