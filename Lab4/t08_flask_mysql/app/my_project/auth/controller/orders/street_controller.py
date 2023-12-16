from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import street_service
from t08_flask_mysql.app.my_project.auth.domain.orders.street import Street
from flask import abort
from typing import List
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class StreetController(GeneralController):

    _service = street_service

    def get_buildings_in_street(self, street_id):
        return street_service.get_buildings_in_street(street_id)
