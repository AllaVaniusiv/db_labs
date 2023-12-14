from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Equipment
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class EquipmentDAO(GeneralDAO):

    _domain_type = Equipment

    def get_employee_with_equipment(self, equipment_id):
        try:
            equipment_objects = self._dao.find_all()

            result = []

            for equipment in equipment_objects:
                if equipment_id is None or equipment.id == equipment_id:
                    employee = equipment.employee
                    
                    workplace = equipment.workplace

                
                    employee_details = self._employee_dao.find_by_employee_id(
                        employee.id)

                    result.append({
                        "employee_id": employee.id,
                        "employee_name": f"{employee.name} {employee.surname}",
                        "phone_number": employee.phone_number,
                        "workplace_id": workplace.id,
                    })

            return result
        except Exception as e:
            print(f"Error: {str(e)}")
