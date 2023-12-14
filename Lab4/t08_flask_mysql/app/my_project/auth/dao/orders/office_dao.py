from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Office
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class OfficeDAO(GeneralDAO):

    _domain_type = Office


    def get_buildings_in_office(self, office_id):
        try:

            office = self.find_by_id(office_id)

            if not office:
                return None

            buildings_in_office = office.buildings

            result = []

            for building in buildings_in_office:
                result.append({
                    "id": building.id,
                    "building_number": building.building_number,
                    "street_id": building.street_id
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

