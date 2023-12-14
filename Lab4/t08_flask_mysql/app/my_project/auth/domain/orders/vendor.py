from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from sqlalchemy import ForeignKey
from t08_flask_mysql.app.my_project import db
from typing import Dict, Any
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class Vendor(db.Model, IDto):
    __tablename__ = "vendor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=True)
    number_phone = db.Column(db.String(45), nullable=True)

    # Define relationship
    equipments = db.relationship('Equipment', backref='vendor')

    def __repr__(self):
        return f"Vendor(id={self.id}, name='{self.name}', address='{self.address}', number_phone='{self.number_phone}')"

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'number_phone': self.number_phone,
        }

    
    @staticmethod
    def create_from_dto(dto_dict):
        obj = Vendor(
            name=dto_dict.get("name"),
            address=dto_dict("address"),
            number_phone=dto_dict("number_phone")
        )
        return obj

