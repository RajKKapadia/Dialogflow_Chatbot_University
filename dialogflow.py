import sys
from flask import Flask
import flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databseSetup import CourseMaster, BranchMaster, FacultyMaster, PlacementMaster, Base

engine = create_engine("sqlite:///unibot_data.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

def courseInfo(course, branch):

    if course != "" and branch != "":
        try:
            data = session.query(BranchMaster).filter(BranchMaster.branch_name == branch).one()
            if course == "Diploma":
                seats = int.from_bytes(data.diploma_seats, byteorder=sys.byteorder)
            elif course == "Degree":
                seats = int.from_bytes(data.degree_seats, byteorder=sys.byteorder)
            elif course == "Master":
                seats = int.from_bytes(data.master_seats, byteorder=sys.byteorder)
            else:
                seats = int.from_bytes(data.phd_seats, byteorder=sys.byteorder)

            if seats == 0:
                outString = "We at this moment don't offer {} in {} Engineering at XYZ College.".format(course, branch)
            else:
                outString = "We offer {} in {} Engineering at XYZ College with {} seats.".format(course, branch, seats)
        except:
            outString = "We don't offer {} in {} Engineering at this moment.".format(course, branch)
    
    return {'fulfillmentText':outString}

def facultyInfo(course, branch):

    try:
        faculties = session.query(FacultyMaster).filter(FacultyMaster.branch_name == branch).all()

        outString = "We have following faculties in {} {} Engineering Department.  \n".format(course, branch)

        for faculty in faculties:
            outString += faculty.faculty_name
            outString += " having "
            outString += faculty.qualification
            outString += " degree and "
            outString += str(int.from_bytes(faculty.experience, byteorder=sys.byteorder))
            outString += " years of experience.  \n"

    except:
        outString = "We don't offer {} in {} Engineering.".format(course, branch)

    return {'fulfillmentText':outString}

def placementInfo(course, branch):
    
    try:
        placements = session.query(PlacementMaster).filter(PlacementMaster.course_name == course,
                                                        PlacementMaster.branch_name == branch).all()
        outString = "Placement data for {} {} Engineering is as follows.  \n".format(course, branch)

        for placement in placements:
            outString += str(int.from_bytes(placement.placed_student, byteorder=sys.byteorder))
            outString += " out of "
            outString += str(int.from_bytes(placement.total_student, byteorder=sys.byteorder))
            outString += " students were placed in different companies during the year "
            outString += str(int.from_bytes(placement.year, byteorder=sys.byteorder))
            outString += ".  \n"
    except:
        outString = "Something went wrong."

    return {'fulfillmentText':outString}

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():

    req = flask.request.get_json(force=True)
    intent = req.get('queryResult').get("intent").get('displayName')
    print(intent)
    course = req.get('queryResult').get("parameters").get('Courses')
    branch = req.get('queryResult').get("parameters").get('Branches')

    if intent == "Courses Intent":
        response = courseInfo(course, branch)
    elif intent == "Faculties Intent":
        response = facultyInfo(course, branch)
    elif intent == "Placement Intent":
        response = placementInfo(course, branch)

    return flask.make_response(flask.jsonify(response))

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()