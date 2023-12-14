from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import city_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.city import City
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class CityService(GeneralService):

    _dao = city_dao

    def get_streets_in_city(self, city_id):
        return city_dao.get_streets_in_city(city_id)
