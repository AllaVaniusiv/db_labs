from t08_flask_mysql.app.my_project.auth.domain import Office
from t08_flask_mysql.app.my_project.auth.controller import office_controller
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")

office_bp = Blueprint('office', __name__, url_prefix='/office')


@office_bp.get('')
def get_all_office() -> Response:
    office = office_controller.find_all()
    return make_response(jsonify(office), HTTPStatus.OK)


@office_bp.post('')
def create_office() -> Response:
    content = request.get_json()
    office = Office.create_from_dto(content)
    office_controller.create(office)
    return make_response(jsonify(office.put_into_dto()), HTTPStatus.CREATED)


@office_bp.get('/<int:office_id>')
def get_office(office_id: int) -> Response:
    office = office_controller.find_by_id(office_id)
    if office:
        return make_response(jsonify(office), HTTPStatus.OK)
    return make_response(jsonify({"error": "Office not found"}), HTTPStatus.NOT_FOUND)


@office_bp.put('/<int:office_id>')
def update_office(place_id: int) -> Response:
    content = request.get_json()
    office = Office.create_from_dto(content)
    office_controller.update(place_id, office)
    return make_response("Office updated", HTTPStatus.OK)


@office_bp.patch('/<int:office_id>')
def patch_office(office_id: int) -> Response:
    content = request.get_json()
    office_controller.patch(office_id, content)
    return make_response("Office updated", HTTPStatus.OK)


@office_bp.delete('/<int:office_id>')
def delete_office(office_id: int) -> Response:
    office_controller.delete(office_id)
    return make_response("Office deleted", HTTPStatus.OK)

@office_bp.get('/get_building/<int:office_id>')
def get_building(office_id):
    return make_response(jsonify(office_controller.get_buildings_in_office(office_id)))
