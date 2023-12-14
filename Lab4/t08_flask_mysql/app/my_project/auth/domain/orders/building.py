import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from sqlalchemy import ForeignKey

class Building(db.Model, IDto):
    __tablename__ = "building"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'), nullable=False)
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'), nullable=False)
    building_number = db.Column(db.Integer, nullable=False)

    # Define relationships
    floors = db.relationship('Floor', backref='building')

    def __repr__(self):
        return f"Building(id={self.id}, office_id={self.office_id}, street_id={self.street_id}, building_number={self.building_number})"

    def put_into_dto(self):
        return {
            'id': self.id,
            'office_id': self.office_id,
            'street_id': self.street_id,
            'building_number': self.building_number,
        }

   
    @staticmethod
    def create_from_dto(dto_dict):
        obj = Building(
            office_id=dto_dict.get("office_id"),
            street_id=dto_dict.get("street_id"),
            building_number=dto_dict.get("building_number"),
        )
        return obj

    