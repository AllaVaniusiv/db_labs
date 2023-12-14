from http import HTTPStatus
from typing import List

from flask import abort
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.domain.orders.type import Type
from t08_flask_mysql.app.my_project.auth.service import type_service
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class TypeController(GeneralController):

    _service = type_service
