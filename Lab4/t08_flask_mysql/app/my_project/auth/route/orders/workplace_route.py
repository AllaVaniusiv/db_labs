import sys
sys.path.append("D:/bd_labs/Lab4_test")
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import workplace_controller
from t08_flask_mysql.app.my_project.auth.domain import Workplace

workplace_bp = Blueprint('workplace', __name__, url_prefix='/workplace')

@workplace_bp.get('')
def get_all_workplace() -> Response:
    workplace = workplace_controller.find_all()
    return make_response(jsonify(workplace), HTTPStatus.OK)

@workplace_bp.post('')
def create_workplace() -> Response:
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.create(workplace)
    return make_response(jsonify(workplace.put_into_dto()), HTTPStatus.CREATED)

@workplace_bp.get('/<int:workplace_id>')
def get_workplace(workplace_id: int) -> Response:
    workplace = workplace_controller.find_by_id(workplace_id)
    if type:
        return make_response(jsonify(workplace), HTTPStatus.OK)
    return make_response(jsonify({"error": "Workplace not found"}), HTTPStatus.NOT_FOUND)

@workplace_bp.put('/<int:workplace_id>')
def update_workplace(workplace_id: int) -> Response:
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.update(workplace_id, workplace)
    return make_response("Workplace updated", HTTPStatus.OK)

@workplace_bp.patch('/<int:workplace_id>')
def patch_workplace(workplace_id: int) -> Response:
    content = request.get_json()
    workplace_controller.patch(workplace_id, content)
    return make_response("Workplace updated", HTTPStatus.OK)

@workplace_bp.delete('/<int:workplace_id>')
def delete_workplace(workplace_id: int) -> Response:
    workplace_controller.delete(workplace_id)
    return make_response("Workplace deleted", HTTPStatus.OK)

@workplace_bp.get('/get_employee/<int:workplace_id>')
def get_employee(workplace_id):
    return make_response(jsonify(workplace_controller.get_employees_in_workplace(workplace_id)))
