# Dialogflow_Chatbot_University [MiningBusinessData]
This is a simple chatbot for university/colleges, it will give information about courses, faculties and placement of that university/college.
- a course and branch is offered or not and if offered then available seats
- faculties info of a course and branch, it also give their education and experience
- placement info of a course and branch, previous years placement


## Pre-requisite :point_right: Python 3.7.3, SQlite, NGROK
- install pipenv
- copy the repository to folder
- cd into folder
- run `pipenv --python 3.7` then `pipenv sync`

Now you are ready...

## Create Database
- run `pipenv run python insertData.py`

this will create unibot_data.db

## NGROK part
- run `ngrok http 5000` in new terminal or if you have downloaded the execuitabel from [NGROK](https://ngrok.com/download)
then you can run `./ngrok http 5000`

It will start a link between your local machine and internet, you copy any of the **forwarding link** as shown in below image.

NGROK terminal view

![NGROK Image](/data/ngrok.png)

## Flask part
- run `pipenv run python dialogflow.py`

this will start a local server, make sure flask server port and ngrok server port is same, if not then stop ngrok and restart
with the port you got from local server by running above code.

## Dialogflow Part
- create new bot
- from bot settings :point_right: Export/Import :point_right: Import from zip upload the Agent.zip
- on main dashboard of agent go to Fullfilments
- Enable webhook
- copy the forwarding link from ngrk terminal and paste there and append /webhook
ngrk-link/webhook

Now you are ready to test the bot.

## What info it will give
This bot can give information on courses, faculties & placement for following Courses and Branches.
- Courses :point_right: Diploma, Degree, Master & PhD (But we can change that for sure)
- Branches :point_right: Automobile, Civil, Computer Science, Electrical, Electronics & Communication, 
Information & Technology, & Mechanical

For information, you can change these from Agent :point_right: Entities.




**Enjoy The Life Feel The Music**
