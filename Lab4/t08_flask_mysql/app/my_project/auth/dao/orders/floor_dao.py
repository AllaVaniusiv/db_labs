from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Floor
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class FloorDAO(GeneralDAO):

    _domain_type = Floor

    
    def get_workplaces_in_floor(self, floor_id):
        try:

            floor = self.find_by_id(floor_id)

            if not floor:
                return None

            workplaces_in_floor = floor.workplaces

            result = []

            for workplace in workplaces_in_floor:
                result.append({
                    "id": workplace.id,
                    "name": workplace.workplace_name,
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None