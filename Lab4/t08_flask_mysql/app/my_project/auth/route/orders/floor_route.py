from t08_flask_mysql.app.my_project.auth.domain import Floor
from t08_flask_mysql.app.my_project.auth.controller import floor_controller
from flask import Blueprint, Response, make_response, jsonify, request
from http import HTTPStatus
import sys
sys.path.append("D:/bd_labs/Lab4_test")


floor_bp = Blueprint('floor', __name__, url_prefix='/floor')


@floor_bp.get('')
def get_all_floor() -> Response:
    floor = floor_controller.find_all()
    return make_response(jsonify(floor), HTTPStatus.OK)


@floor_bp.post('')
def create_floor() -> Response:
    content = request.get_json()
    floor = Floor.create_from_dto(content)
    floor_controller.create(floor)
    return make_response(jsonify(floor.put_into_dto()), HTTPStatus.CREATED)


@floor_bp.get('/<int:floor_id>')
def get_floor(floor_id: int) -> Response:
    floor = floor_controller.find_by_id(floor_id)
    if floor:
        return make_response(jsonify(floor), HTTPStatus.OK)
    return make_response(jsonify({"error": "Floor not found"}), HTTPStatus.NOT_FOUND)


@floor_bp.put('/<int:floor_id>')
def update_floor(floor_id: int) -> Response:
    content = request.get_json()
    floor = floor.create_from_dto(content)
    floor_controller.update(floor_id, floor)
    return make_response("Floor updated", HTTPStatus.OK)


@floor_bp.patch('/<int:floor_id>')
def patch_floor(floor_id: int) -> Response:
    content = request.get_json()
    floor_controller.patch(floor_id, content)
    return make_response("Floor updated", HTTPStatus.OK)


@floor_bp.delete('/<int:floor_id>')
def delete_floor(floor_id: int) -> Response:
    floor_controller.delete(floor_id)
    return make_response("Floor deleted", HTTPStatus.OK)

@floor_bp.get('/get_workplace/<int:floor_id>')
def get_workplace(floor_id):
    return make_response(jsonify(floor_controller.get_workplaces_in_floor(floor_id)))