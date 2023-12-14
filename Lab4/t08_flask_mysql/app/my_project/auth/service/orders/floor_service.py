from t08_flask_mysql.app.my_project.auth.domain.orders.floor import Floor
from typing import List
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import floor_dao
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class FloorService(GeneralService):

    _dao = floor_dao

    def get_workplaces_in_floor(self, floor_id):
        return floor_dao.get_workplaces_in_floor(floor_id)

