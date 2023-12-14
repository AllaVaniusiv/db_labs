from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Building
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class BuildingDAO(GeneralDAO):

    _domain_type = Building

    def get_floors_in_building(self, building_id):
        try:

            building = self.find_by_id(building_id)

            if not building:
                return None

            floors_in_building = building.floors

            result = []

            for floor in floors_in_building:
                result.append({
                    "id": floor.id,
                    "number": floor.number,
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
