import sys
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto


class Equipment(db.Model, IDto):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    serial_number = db.Column(db.String(45), nullable=True)
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'employee.id'), nullable=False)
    workplace_id = db.Column(db.Integer, db.ForeignKey(
        'workplace.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey(
        'vendor.id'), nullable=False)


    def __repr__(self) -> str:
        return f"Equipment(id={self.id}, name='{self.name}', serial_number='{self.serial_number}', employee_id={self.employee_id}, workplace_id={self.workplace_id}, type_id={self.type_id}, vendor_id={self.vendor_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'serial_number': self.serial_number,
            'employee_id': self.employee_id,
            'workplace_id': self.workplace_id,
            'type_id': self.type_id,
            'vendor_id': self.vendor_id,
        }

    @staticmethod
    def create_from_dto(equipment_dict: Dict[str, Any]):
        return Equipment(**equipment_dict)
