from flask import abort
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import building_service
from t08_flask_mysql.app.my_project.auth.domain.orders.building import Building
from t08_flask_mysql.app.my_project.auth.dao.orders.building_dao import BuildingDAO
from http import HTTPStatus
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class BuildingController(GeneralController):

    _service = building_service

    def get_floors_in_building(self, building_id):
        return building_service.get_floors_in_building(building_id)
