from .error_handler import err_handler_bp

from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .orders.building_route import building_bp
    from .orders.city_route import city_bp
    from .orders.department_route import department_bp
    from .orders.employee_route import employee_bp
    from .orders.floor_route import floor_bp
    from .orders.office_route import office_bp
    from .orders.street_route import street_bp
    from .orders.type_route import type_bp
    from .orders.vendor_route import vendor_bp
    from .orders.workplace_route import workplace_bp
    from .orders.equipment_route import equipment_bp


    app.register_blueprint(building_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(floor_bp)
    app.register_blueprint(office_bp)
    app.register_blueprint(street_bp)
    app.register_blueprint(type_bp)
    app.register_blueprint(vendor_bp)
    app.register_blueprint(workplace_bp)
    app.register_blueprint(equipment_bp)