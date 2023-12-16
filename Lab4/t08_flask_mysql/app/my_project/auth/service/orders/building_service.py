from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.domain import Building
from t08_flask_mysql.app.my_project.auth.dao import building_dao
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class BuildingService(GeneralService):

    _dao = building_dao
    
    def get_floors_in_building(self, building_id):
        return building_dao.get_floors_in_building(building_id)