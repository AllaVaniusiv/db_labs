from t08_flask_mysql.app.my_project.auth.domain import Department
from t08_flask_mysql.app.my_project.auth.controller import department_controller
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")

department_bp = Blueprint('department', __name__, url_prefix='/department')


@department_bp.get('')
def get_all_department() -> Response:
    print("finding owners")
    department = department_controller.find_all()
    return make_response(jsonify(department), HTTPStatus.OK)


@department_bp.post('')
def create_department() -> Response:
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.create(department)
    return make_response(jsonify(department.put_into_dto()), HTTPStatus.CREATED)


@department_bp.get('/<int:department_id>')
def get_department(department_id: int) -> Response:
    department = department_controller.find_by_id(department_id)
    if department:
        return make_response(jsonify(department), HTTPStatus.OK)
    return make_response(jsonify({"error": "Department not found"}), HTTPStatus.NOT_FOUND)


@department_bp.put('/<int:department_id>')
def update_department(department_id: int) -> Response:
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.update(department_id, department)
    return make_response("Department updated", HTTPStatus.OK)


@department_bp.patch('/<int:department_id>')
def patch_department(department_id: int) -> Response:
    content = request.get_json()
    department_controller.patch(department_id, content)
    return make_response("Department updated", HTTPStatus.OK)


@department_bp.delete('/<int:department_id>')
def delete_department(department_id: int) -> Response:
    department_controller.delete(department_id)
    return make_response("Department deleted", HTTPStatus.OK)
