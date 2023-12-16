from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project import db
from typing import Dict, Any
import sys
sys.path.append("D:/bd_labs/Lab4_test")


class Type(db.Model, IDto):
    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return f"Type(id={self.id}, name='{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def create_from_dto(type_dict: Dict[str, Any]):
        return Type(**type_dict)
