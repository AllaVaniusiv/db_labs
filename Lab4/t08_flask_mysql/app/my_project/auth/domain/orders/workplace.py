import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto

class Workplace(db.Model, IDto):
    __tablename__ = "workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)
    workplace_name = db.Column(db.String(45), nullable=True)

    # Define relationships
    employees = relationship('Employee', backref='workplace')

    def __repr__(self):
        return f"Workplace(id={self.id}, floor_id={self.floor_id}, workplace_name='{self.workplace_name}')"

    def put_into_dto(self):
        return {
            'id': self.id,
            'floor_id': self.floor_id,
            'workplace_name': self.workplace_name,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Workplace(
            floor_id=dto_dict.get("name"),
            workplace_name=dict.get("workplace_name")
        )
        return obj
