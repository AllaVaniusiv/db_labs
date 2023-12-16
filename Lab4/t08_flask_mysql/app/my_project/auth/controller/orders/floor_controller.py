from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import floor_service
from t08_flask_mysql.app.my_project.auth.domain.orders.floor import Floor
from flask import abort
from typing import List
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class FloorController(GeneralController):

    _service = floor_service

    def get_workplaces_in_floor(self, floor_id):
        return floor_service.get_workplaces_in_floor(floor_id)
