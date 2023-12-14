from t08_flask_mysql.app.my_project.auth.domain import Employee
from t08_flask_mysql.app.my_project.auth.controller import employee_controller
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


employee_bp = Blueprint('employee', __name__, url_prefix='/employee')


@employee_bp.get('')
def get_all_city() -> Response:
    employee = employee_controller.find_all()
    return make_response(jsonify(employee), HTTPStatus.OK)


@employee_bp.post('')
def create_employee() -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)


@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    employee = employee_controller.find_by_id(employee_id)
    if employee:
        return make_response(jsonify(employee), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)


@employee_bp.put('/<int:employee_id>')
def update_city(employee_id: int) -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.patch('/<int:employee_id>')
def patch_employee(employee_id: int) -> Response:
    content = request.get_json()
    employee_controller.patch(employee_id, content)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.delete('/<int:employee_id>')
def delete_city(employee_id: int) -> Response:
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)
