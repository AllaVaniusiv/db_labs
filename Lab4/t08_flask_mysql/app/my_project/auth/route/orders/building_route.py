from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import building_controller
from t08_flask_mysql.app.my_project.auth.dao import building_dao
from t08_flask_mysql.app.my_project.auth.domain import Building
import sys
sys.path.append("D:/bd_labs/Lab4_test")

building_bp = Blueprint('building', __name__, url_prefix='/building')


@building_bp.get('')
def get_all_building() -> Response:
    building = building_controller.find_all()
    return make_response(jsonify(building), HTTPStatus.OK)


@building_bp.post('')
def create_building() -> Response:
    content = request.get_json()
    building = Building.create_from_dto(content)
    building_controller.create(building)
    return make_response(jsonify(building.put_into_dto()), HTTPStatus.CREATED)


@building_bp.get('/<int:building_id>')
def get_building(building_id: int) -> Response:
    building = building_controller.find_by_id(building_id)
    if building:
        return make_response(jsonify(building), HTTPStatus.OK)
    return make_response(jsonify({"error": "Building not found"}), HTTPStatus.NOT_FOUND)


@building_bp.put('/<int:building_id>')
def update_building(building_id: int) -> Response:
    content = request.get_json()
    building = Building.create_from_dto(content)
    building_controller.update(building_id, building)
    return make_response("Building updated", HTTPStatus.OK)


@building_bp.patch('/<int:building_id>')
def patch_building(building_id: int) -> Response:
    content = request.get_json()
    building_controller.patch(building_id, content)
    return make_response("Building updated", HTTPStatus.OK)


@building_bp.delete('/<int:building_id>')
def delete_building(building_id: int) -> Response:
    building_controller.delete(building_id)
    return make_response("Building deleted", HTTPStatus.OK)

@building_bp.get('/get_floor/<int:building_id>')
def get_floor(building_id):
    return make_response(jsonify(building_controller.get_floors_in_building(building_id)))
