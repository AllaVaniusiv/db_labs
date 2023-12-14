from .orders.building_service import BuildingService
from .orders.city_service import CityService
from .orders.department_service import DepartmentService
from .orders.employee_service import EmployeeService
from .orders.floor_service import FloorService
from .orders.office_service import OfficeService
from .orders.street_service import StreetService
from .orders.type_service import TypeService
from .orders.vendor_service import VendorService
from .orders.workplace_service import WorkplaceService
from .orders.equipment_service import EquipmentService



building_service = BuildingService()
city_service = CityService()
department_service = DepartmentService()
employee_service = EmployeeService()
floor_service = FloorService()
office_service = OfficeService()
street_service = StreetService()
type_service = TypeService()
vendor_service = VendorService()
workplace_service = WorkplaceService()
equipment_service = EquipmentService()