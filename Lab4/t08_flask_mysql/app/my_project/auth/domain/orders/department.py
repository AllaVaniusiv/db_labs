import sys
sys.path.append("D:/bd_labs/Lab4_test")
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project.auth.domain.general_domain import IDto

class Department(db.Model, IDto):
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    date_create = db.Column(db.Date, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)


    def __repr__(self) -> str:
        return f"Department(id={self.id}, name='{self.name}', date_create={self.date_create}, employee_id={self.employee_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'date_create': str(self.date_create),
            'employee_id': self.employee_id,
        }

    @staticmethod
    def create_from_dto(department_dict: Dict[str, Any]):
        return Department(**department_dict)