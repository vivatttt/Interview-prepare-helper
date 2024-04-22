<p align="center">
  <img src="https://i.ibb.co/GnsVqRd/image.png" width=500>
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Flask-3.0.3-purple">
   <img src="https://img.shields.io/badge/SQLAlchemy-2.0.29-red">
</p>


## About
This website was created to help people prepare for interviews in IT companies<br>
It is proposed to recreate the process of **a real interview** between two candidates - one of them will be an interviewer and will conduct the interview, and the other will be passing it it
<br><br>
The website features two main functions:
1. Register the interviewer for a specific date and time to conduct an interview at that time
2. For the interviewee, find a suitable interviewer based on required programming language and desired date
## Demonstration
<p align="center">
      <img src="https://github.com/vivatttt/Interview-prepare-helper/blob/master/demonstration.gif">
</p>

## Getting started
To launch the **Interview Prepare Helper** run following on your **Linux** PC

Download the Virtual Enviroment
```shell
python3 -m venv env
```
```shell
source env/bin/activate
```
Then install all the necessary frameworks
```shell
pip install -r requirements.txt
```
Then you need to initialize DataBase on your PC<br>
So:
1. Create database.db in main directory
2. Run following:
   
```shell
flask db init
flask db migrate -m "initial migration"
flask db upgrade
 ```
And finally <br>
```shell
make run
```
And enjoy `localhost:8000`
## Gallery <br>

<p align="center">
      <img src="https://i.ibb.co/Ph4r3YZ/image.png" alt = "Start page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/dGhpMFR/image.png" alt = "Interviewer page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/y5xpKQj/image.png" alt = "Interviewee page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/fY8320M/image.png" alt = "Interview scheduled" width="900">
</p>

