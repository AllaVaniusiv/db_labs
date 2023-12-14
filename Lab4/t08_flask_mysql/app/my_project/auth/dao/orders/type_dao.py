from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Type
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class TypeDAO(GeneralDAO):

    _domain_type = Type
