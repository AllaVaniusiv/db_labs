from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from t08_flask_mysql.app.my_project import db
from typing import Dict, Any
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class City(db.Model):
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    # Define relationship
    streets = db.relationship('Street', backref='city')

    def __repr__(self):
        return f"City(id={self.id}, name='{self.name}')"

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = City(
            name=dto_dict.get("name"),
        )
        return obj
