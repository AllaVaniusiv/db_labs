from typing import List
from t08_flask_mysql.app.my_project.auth.domain import City
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class CityDAO(GeneralDAO):

    _domain_type = City

    def get_streets_in_city(self, city_id):
        try:

            city = self.find_by_id(city_id)

            if not city:
                return None

            streets_in_city = city.streets

            result = []

            for street in streets_in_city:
                result.append({
                    "id": street.id,
                    "name": street.name,
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
