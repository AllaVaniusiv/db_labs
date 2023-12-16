import sys
sys.path.append("D:/bd_labs/Lab4_test")
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import vendor_controller
from t08_flask_mysql.app.my_project.auth.domain import Vendor

vendor_bp = Blueprint('vendor', __name__, url_prefix='/vendor')

@vendor_bp.get('')
def get_all_vendor() -> Response:
    vendor = vendor_controller.find_all()
    return make_response(jsonify(vendor), HTTPStatus.OK)

@vendor_bp.post('')
def create_vendor() -> Response:
    content = request.get_json()
    vendor = Vendor.create_from_dto(content)
    vendor_controller.create(vendor)
    return make_response(jsonify(vendor.put_into_dto()), HTTPStatus.CREATED)

@vendor_bp.get('/<int:vendor_id>')
def get_vendor(vendor_id: int) -> Response:
    vendor = vendor_controller.find_by_id(vendor_id)
    if type:
        return make_response(jsonify(vendor), HTTPStatus.OK)
    return make_response(jsonify({"error": "Vendor not found"}), HTTPStatus.NOT_FOUND)


@vendor_bp.put('/<int:vendor_id>')
def update_vendor(vendor_id: int) -> Response:
    content = request.get_json()
    vendor = Vendor.create_from_dto(content)
    vendor_controller.update(vendor_id, vendor)
    return make_response("Vendor updated", HTTPStatus.OK)

@vendor_bp.patch('/<int:vendor_id>')
def patch_vendor(vendor_id: int) -> Response:
    content = request.get_json()
    vendor_controller.patch(vendor_id, content)
    return make_response("Vendor updated", HTTPStatus.OK)

@vendor_bp.delete('/<int:vendor_id>')
def delete_vendor(vendor_id: int) -> Response:
    vendor_controller.delete(vendor_id)
    return make_response("Vendor deleted", HTTPStatus.OK)

@vendor_bp.get('/get_equipment/<int:vendor_id>')
def get_equipment(vendor_id):
    return make_response(jsonify(vendor_controller.get_equipments_in_vendor(vendor_id)))