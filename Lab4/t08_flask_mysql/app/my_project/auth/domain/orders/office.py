import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from sqlalchemy import ForeignKey
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto

class Office(db.Model, IDto):
    __tablename__ = "office"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    # Define relationship
    buildings = db.relationship('Building', backref='office')

    def __repr__(self):
        return f"Office(id={self.id}, name='{self.name}')"

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Office(
            name=dto_dict.get("name"),
        )
        return obj
