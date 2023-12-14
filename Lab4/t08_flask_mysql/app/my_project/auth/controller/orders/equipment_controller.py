from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import equipment_service
from t08_flask_mysql.app.my_project.auth.domain.orders.equipment import Equipment
from flask import abort
from http import HTTPStatus
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class EquipmentController(GeneralController):

    _service = equipment_service
    
    def get_employee_with_equipment(self, employee_id):
        return self._service.get_employee_with_equipment(employee_id)