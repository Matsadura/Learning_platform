"""Holds the Solution_Result class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Solution_Result(BaseModel, Base):
    """Representation of a solution result"""
    __tablename__ = 'solution_results'
    submission_id = Column(String(128),
                           ForeignKey('submissions.id', ondelete='CASCADE'),
                           nullable=False)
    task_test_case_id = Column(String(128), nullable=False)
    output = Column(Enum('pass', 'fail', 'error'), nullable=False)
    submission = relationship("Submission", back_populates="solution_results",)


def __init__(self, *args, **kwargs):
    """initializes solution result"""
    super().__init__(*args, **kwargs)
