from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import vendor_service
from http import HTTPStatus
import sys
from typing import List

from flask import abort
from t08_flask_mysql.app.my_project.auth.domain.orders.vendor import Vendor
sys.path.append("D:/bd_labs/Lab4_test")


class VendorController(GeneralController):

    _service = vendor_service

    
    def get_equipments_in_vendor(self, vendor_id):
        return vendor_service.get_equipments_in_vendor(vendor_id)