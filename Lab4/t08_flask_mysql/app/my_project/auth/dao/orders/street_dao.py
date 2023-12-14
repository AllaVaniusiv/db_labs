from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Street
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class StreetDAO(GeneralDAO):
    
    _domain_type = Street

    
    def get_buildings_in_street(self, street_id):
        try:

            street = self.find_by_id(street_id)

            if not street:
                return None

            buildings_in_street = street.buildings

            result = []

            for building in buildings_in_street:
                result.append({
                    "id": building.id,
                    "office_id": building.office_id,
                    "building_number": building.building_number
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

