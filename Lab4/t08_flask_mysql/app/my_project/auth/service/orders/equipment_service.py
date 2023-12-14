from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import equipment_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.equipment import Equipment
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class EquipmentService(GeneralService):

    _dao = equipment_dao

    def get_employee_with_equipment(self, employee_id):
        return self._dao.get_employee_with_equipment(employee_id)
