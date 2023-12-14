import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Floor(db.Model,IDto):
    __tablename__ = "floor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # Define relationship
    workplaces = relationship('Workplace', backref='floor')

    def __repr__(self) -> str:
        return f"Floor(id={self.id}, building_id={self.building_id}, number={self.number})"

    def put_into_dto(self):
        return {
            'id': self.id,
            'building_id': self.building_id,
            'number': self.number,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Floor(
            building_id=dto_dict.get("building_id"),
            number=dto_dict.get("number")
        )
        return obj
