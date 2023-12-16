from t08_flask_mysql.app.my_project.auth.domain.orders.office import Office
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import office_dao
from typing import List
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class OfficeService(GeneralService):

    _dao = office_dao

    def get_buildings_in_office(self, office_id):
        return office_dao.get_buildings_in_office(office_id)
