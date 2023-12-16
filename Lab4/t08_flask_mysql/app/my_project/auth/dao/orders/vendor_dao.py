from typing import List
from t08_flask_mysql.app.my_project.auth.domain import Vendor
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class VendorDAO(GeneralDAO):

    _domain_type = Vendor

    
    def get_equipments_in_vendor(self, vendor_id):
        try:

            vendor = self.find_by_id(vendor_id)

            if not vendor:
                return None

            equipments_in_vendor = vendor.equipments

            result = []

            for equipment in equipments_in_vendor:
                result.append({
                    "id": equipment.id,
                    "name": equipment.name,
                    "serial_number": equipment.serial_number,
                    "employee_id": equipment.employee_id,
                    "workplace_id": equipment.workplace_id,
                    "type_id": equipment.type_id,
                })

            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

