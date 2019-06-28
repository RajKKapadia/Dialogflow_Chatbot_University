from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy import ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class CourseMaster(Base):

    """ Creates a course_master table in database
        id --> Integer
        course_name --> String
    """

    __tablename__ = 'course_master'
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)

    @property
    def serialize(self):

        return{
            'id':self.id,
            'course_name':self.course_name,
        }

class BranchMaster(Base):

    """ Creates a branch_master table in database
        id --> Integer
        branch_name --> String
        diploma_seats --> Integer
        degree_seats --> Integer
        master_seats --> Integer
        phd_seats --> Integer
    """
    __tablename__ = 'branch_master'
    id = Column(Integer, primary_key=True)
    branch_name = Column(String, nullable=False)
    diploma_seats = Column(Integer, nullable=False)
    degree_seats = Column(Integer, nullable=False)
    master_seats = Column(Integer, nullable=False)
    phd_seats = Column(Integer, nullable=False)

    @property
    def serialize(self):

        return{
            'id':self.id,
            'branch_name':self.branch_name,
            'diploma_seats':self.diploma_seats,
            'degree_seats':self.degree_seats,
            'master_seats':self.master_seats,
            'phd_seats':self.phd_seats,
        }

class FacultyMaster(Base):

    """ Create faculty_master table in database
        id --> Integer
        faculty_name --> String
        qualification --> String
        experience --> Integer
        is_diploma --> Integer (0 = Teaching, 1 = Not Teaching)
        is_degree --> Integer
        is_master --> Integer
        is_phd --> Integer
        branch_name --> String
    """

    __tablename__ = 'faculty_master'
    id = Column(Integer, primary_key=True)
    faculty_name = Column(String, nullable=False)
    qualification = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)
    is_diploma = Column(Boolean, nullable=False)
    is_degree = Column(Boolean, nullable=False)
    is_master = Column(Boolean, nullable=False)
    is_phd = Column(Boolean, nullable=False)
    branch_name = Column(String, nullable=False)

    @property
    def serialize(self):

        return{
            'id':self.id,
            'name':self.name,
            'qualification':self.qualification,
            'experience':self.experience,
            'is_diploma':self.is_diploma,
            'is_degree':self.is_degree,
            'is_phd':self.is_phd,
            'is_master':self.is_master,
            'branch_name':self.branch_name,
        }

class PlacementMaster(Base):
    
    """ Create placement_master table in database
        id --> Integer
        placed_student --> Integer
        total_student --> Intger
        year --> Integer
        course_name --> String
        branch_name --> String
    """

    __tablename__ = 'placement_master'
    id = Column(Integer, primary_key=True)
    placed_student = Column(Integer, nullable=False)
    total_student = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    course_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)

    @property
    def serialize(self):

        return{
            'id':self.id,
            'placed_student':self.placed_student,
            'total_student':self.total_student,
            'year':self.year,
            'course_name':self.course_name,
            'branch_name':self.branch_name,
        }

engine = create_engine('sqlite:///unibot_data.db')
Base.metadata.create_all(engine)