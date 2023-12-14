from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.domain import City
from t08_flask_mysql.app.my_project.auth.service import city_service
from flask import abort
from typing import List
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class CityController(GeneralController):

    _service = city_service

    def get_streets_in_city(self, city_id):
        return city_service.get_streets_in_city(city_id)