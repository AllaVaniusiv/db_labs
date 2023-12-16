from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import street_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.street import Street
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class StreetService(GeneralService):

    _dao = street_dao

    def get_buildings_in_street(self, street_id):
        return street_dao.get_buildings_in_street(street_id)

