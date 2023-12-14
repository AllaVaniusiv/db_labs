from t08_flask_mysql.app.my_project.auth.domain import Equipment
from t08_flask_mysql.app.my_project.auth.controller import equipment_controller
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


equipment_bp = Blueprint('equipment', __name__, url_prefix='/equipment')


@equipment_bp.get('')
def get_all_equipment() -> Response:
    equipment = equipment_controller.find_all()
    return make_response(jsonify(equipment), HTTPStatus.OK)


@equipment_bp.post('')
def create_equipment() -> Response:
    content = request.get_json()
    equipment = equipment.create_from_dto(content)
    equipment_controller.create(equipment)
    return make_response(jsonify(equipment.put_into_dto()), HTTPStatus.CREATED)


@equipment_bp.get('/<int:equipment_id>')
def get_equipment(equipment_id: int) -> Response:
    equipment = equipment_controller.find_by_id(equipment_id)
    if equipment:
        return make_response(jsonify(equipment), HTTPStatus.OK)
    return make_response(jsonify({"error": "Equipment not found"}), HTTPStatus.NOT_FOUND)


@equipment_bp.put('/<int:equipment_id>')
def update_city(equipment_id: int) -> Response:
    content = request.get_json()
    equipment = Equipment.create_from_dto(content)
    equipment_controller.update(equipment_id, equipment)
    return make_response("equipment updated", HTTPStatus.OK)


@equipment_bp.patch('/<int:equipment_id>')
def patch_equipment(equipment_id: int) -> Response:
    content = request.get_json()
    equipment_controller.patch(equipment_id, content)
    return make_response("equipment updated", HTTPStatus.OK)


@equipment_bp.delete('/<int:equipment_id>')
def delete_city(equipment_id: int) -> Response:
    equipment_controller.delete(equipment_id)
    return make_response("equipment deleted", HTTPStatus.OK)

@equipment_bp.get('/employees/<int:equipment_id>')
def get_employee_with_equipment(equipment_id: int) -> Response:
    try:
        employee_with_equipment = equipment_controller.get_employee_with_equipment(equipment_id)
        return make_response(jsonify(employee_with_equipment), HTTPStatus.OK)
    except Exception as e:
        print(f"Error: {str(e)}")
        return make_response(jsonify({"error": "Internal Server Error"}), HTTPStatus.INTERNAL_SERVER_ERROR)
