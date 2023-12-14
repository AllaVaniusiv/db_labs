from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from sqlalchemy import ForeignKey
from t08_flask_mysql.app.my_project import db
from typing import Dict, Any
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class Street(db.Model, IDto):
    __tablename__ = "street"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    # Define relationship
    buildings = db.relationship('Building', backref='street')

    def __repr__(self):
        return f"Street(id={self.id}, name='{self.name}', city_id={self.city_id})"

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'city_id': self.city_id,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Street(
            name=dto_dict.get("name"),
            city_id=dto_dict.get("city_id"),
        )
        return obj
