from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from databseSetup import CourseMaster, BranchMaster, FacultyMaster, PlacementMaster, Base

# Create engine
engine = create_engine('sqlite:///unibot_data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Read the csv files
course_data = pd.read_csv("data/Course_Data.csv")
branch_data = pd.read_csv("data/Branch_Data.csv")
faculty_data = pd.read_csv("data/Faculty_Data.csv")
placement_data = pd.read_csv("data/Placement_Data.csv")

for i in range(len(course_data)):
    course_name = course_data.course_name.iloc[i]
    course = CourseMaster(course_name=course_name)
    session.add(course)
    session.commit()

for i in range(len(branch_data)):
    branch_name = branch_data.branch_name.iloc[i]
    diploma_seats = branch_data.diploma_seats.iloc[i]
    degree_seats = branch_data.degree_seats.iloc[i]
    master_seats = branch_data.master_seats.iloc[i]
    phd_seats = branch_data.phd_seats.iloc[i]
    branch = BranchMaster(branch_name=branch_name, diploma_seats=diploma_seats,
                        degree_seats=degree_seats, master_seats=master_seats,
                        phd_seats=phd_seats)
    session.add(branch)
    session.commit()

for i in range(len(faculty_data)):
    faculty_name = faculty_data.faculty_name.iloc[i]
    qualification = faculty_data.qualification.iloc[i]
    experience = faculty_data.experience.iloc[i]
    is_diploma = faculty_data.is_diploma.iloc[i]
    is_degree = faculty_data.is_degree.iloc[i]
    is_master = faculty_data.is_master.iloc[i]
    is_phd = faculty_data.is_phd.iloc[i]
    branch_name = faculty_data.branch_name.iloc[i]
    faculty = FacultyMaster(faculty_name=faculty_name, qualification=qualification,
                            experience=experience, is_diploma=is_diploma, is_degree=is_degree,
                            is_master=is_master, is_phd=is_phd, branch_name=branch_name)
    session.add(faculty)
    session.commit()

for i in range(len(placement_data)):
    placed_student = placement_data.placed_student.iloc[i]
    total_student = placement_data.total_student.iloc[i]
    year = placement_data.year.iloc[i]
    course_name = placement_data.course_name.iloc[i]
    branch_name = placement_data.branch_name.iloc[i]
    placement = PlacementMaster(placed_student=placed_student, total_student=total_student,
                                year=year, course_name=course_name, branch_name=branch_name)
    session.add(placement)
    session.commit()

print("All data dded successfully.")