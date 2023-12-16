from t08_flask_mysql.app.my_project.auth.domain import Street
from t08_flask_mysql.app.my_project.auth.controller import street_controller
from flask import Blueprint, Response, make_response, jsonify, request
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")

street_bp = Blueprint('street', __name__, url_prefix='/street')


@street_bp.get('')
def get_all_street() -> Response:
    street = street_controller.find_all()
    return make_response(jsonify(street), HTTPStatus.OK)


@street_bp.post('')
def create_street() -> Response:
    content = request.get_json()
    street = Street.create_from_dto(content)
    street_controller.create(street)
    return make_response(jsonify(street.put_into_dto()), HTTPStatus.CREATED)


@street_bp.get('/<int:street_id>')
def get_street(street_id: int) -> Response:
    street = street_controller.find_by_id(street_id)
    if street:
        return make_response(jsonify(street), HTTPStatus.OK)
    return make_response(jsonify({"error": "Street not found"}), HTTPStatus.NOT_FOUND)


@street_bp.put('/<int:street_id>')
def update_street(street_id: int) -> Response:
    content = request.get_json()
    street = Street.create_from_dto(content)
    street_controller.update(street_id, street)
    return make_response("Street updated", HTTPStatus.OK)


@street_bp.patch('/<int:street_id>')
def patch_street(street_id: int) -> Response:
    content = request.get_json()
    street_controller.patch(street_id, content)
    return make_response("Street updated", HTTPStatus.OK)


@street_bp.delete('/<int:street_id>')
def delete_street(street_id: int) -> Response:
    street_controller.delete(street_id)
    return make_response("Street deleted", HTTPStatus.OK)

@street_bp.get('/get_building/<int:street_id>')
def get_building(street_id):
    return make_response(jsonify(street_controller.get_buildings_in_street(street_id)))