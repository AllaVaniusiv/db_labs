from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Workplace
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class WorkplaceDAO(GeneralDAO):

    _domain_type = Workplace
    
    def get_employees_in_workplace(self, workplace_id):
        try:

            workplace = self.find_by_id(workplace_id)

            if not workplace:
                return None

            employees_in_workplace = workplace.employees

            result = []

            for employee in employees_in_workplace:
                result.append({
                    "id": employee.id,
                    "name": employee.name,
                    "surname": employee.surname,
                    "phone_number": employee.phone_number
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
