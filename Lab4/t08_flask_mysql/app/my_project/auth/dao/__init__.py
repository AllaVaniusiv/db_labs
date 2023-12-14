from .orders.building_dao import BuildingDAO
from .orders.city_dao import CityDAO
from .orders.department_dao import DepartmentDAO
from .orders.employee_dao import EmployeeDAO
from .orders.floor_dao import FloorDAO
from .orders.office_dao import OfficeDAO
from .orders.street_dao import StreetDAO
from .orders.type_dao import TypeDAO
from .orders.vendor_dao import VendorDAO
from .orders.workplace_dao import WorkplaceDAO
from .orders.equipment_dao import EquipmentDAO

building_dao = BuildingDAO()
city_dao = CityDAO()
department_dao = DepartmentDAO()
employee_dao = EmployeeDAO()
floor_dao = FloorDAO()
office_dao = OfficeDAO()
street_dao = StreetDAO()
type_dao = TypeDAO()
vendor_dao = VendorDAO()
workplace_dao = WorkplaceDAO()
equipment_dao = EquipmentDAO()