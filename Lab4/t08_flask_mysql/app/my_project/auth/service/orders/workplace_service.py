from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import workplace_dao
import sys
from typing import List

from t08_flask_mysql.app.my_project.auth.domain.orders.workplace import Workplace
sys.path.append("D:/bd_labs/Lab4_test")


class WorkplaceService(GeneralService):

    _dao = workplace_dao

    def get_employees_in_workplace(self, workplace_id):
        return workplace_dao.get_employees_in_workplace(workplace_id)

