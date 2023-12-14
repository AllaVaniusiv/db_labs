import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto

class Employee(db.Model, IDto):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True)
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)


    # # Define relationships
    # workplace = relationship('Workplace', back_populates='employee')
    # department = relationship('Department', back_populates='employee')
    # equipment = relationship('Equipment', back_populates='employee')

    def __repr__(self) -> str:
        return f"Employee(id={self.id}, name='{self.name}', surname='{self.surname}', phone_number='{self.phone_number}', workplace_id={self.workplace_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone_number': self.phone_number,
            'workplace_id': self.workplace_id,
        }

    @staticmethod
    def create_from_dto(employee_dict: Dict[str, Any]):
        return Employee(**employee_dict)