from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import type_dao
import sys
from typing import List

from t08_flask_mysql.app.my_project.auth.domain.orders.type import Type
sys.path.append("D:/bd_labs/Lab4_test")


class TypeService(GeneralService):

    _dao = type_dao

