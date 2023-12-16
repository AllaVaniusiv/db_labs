import sys
from typing import List

from t08_flask_mysql.app.my_project.auth.domain.orders.vendor import Vendor
sys.path.append("D:/bd_labs/Lab4_test")
from t08_flask_mysql.app.my_project.auth.dao import vendor_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class VendorService(GeneralService):
    
    _dao = vendor_dao

    def get_equipments_in_vendor(self, vendor_id):
        return vendor_dao.get_equipments_in_vendor(vendor_id)
