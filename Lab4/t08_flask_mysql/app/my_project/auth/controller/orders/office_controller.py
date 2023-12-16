from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import office_service
from t08_flask_mysql.app.my_project.auth.domain.orders.office import Office
from flask import abort
from typing import List
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class OfficeController(GeneralController):

    _service = office_service

    def get_buildings_in_office(self, office_id):
        return office_service.get_buildings_in_office(office_id)
