## stackS-api

[![Build Status](https://travis-ci.org/hogum/stackS-api.svg?branch=develop)](https://travis-ci.org/hogum/stackS-api)
[![Coverage Status](https://coveralls.io/repos/github/hogum/stackS-api/badge.png?branch=develop)](https://coveralls.io/github/hogum/stackS-api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/026466004435ebedbdf8/maintainability)](https://codeclimate.com/github/hogum/stackS-api/maintainability)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/faa1bb2518cd81a3e91d)


stackS is a platform where human beings can ask questions and provide answers to present questions.

### What it can do
- Users can create an account and log in.
- Users can post questions.
- Users can delete the questions they post.
- Users can post answers.
- Users can view the answers to questions.
- Users can accept an answer out of all the answers to their question as the preferred answer. 

## API
### Installation
- Clone the repository
```shell
$ git clone https://github.com/hogum/stackS-api.git
```
- Switch to the stackS directory
```shell
$ cd stackS-api
```
- Depending on your os open your virtual enviroment
- Install the project requirements
```shell
$ pip install -r requirements.txt
```

### Running the application
```shell 
$ export FLASK_APP=app
```
or
```shell
$ set FLASK_APP=app
```
on Windows OS
##### Start the server
``` shell
$ flask run
```

### Project Dependencies
- [Flask](http://flask.pocoo.org/)

### Endpoints

##### Authorization Endpoints

Method | Endpoint | Functionality
--- | --- |---
POST | `api/v1/auth/register` | Register new User
POST | `api/v1/auth/login` | Login registered User
PUT | `api/v1/auth/users/user_id` | Update user details
DELETE | `api/v1/auth/users/user_id` | Delete a user account
GET | `api/v1/auth/users` | Get all registered users
GET | `api/v1/auth/users/user_id` | Get a single user



##### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions 
GET | `/api/v1/questions/question_id` | Retrieve a question 
PUT | `/api/v1/questions/question_id` | Edit a question of a logged in user
DELETE | `/api/v1/questions/question_id` | Delete a request of a logged in user



##### Answers Endpoints


Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/question_id/answers` | Add an answer
GET | `/api/v1/questions/question_id/answers` | Lists all answers 
GET | `/api/v1/questions/question_id/answers/answerID` | Retrieve an answers 
PUT | `/api/v1/questions/question_id/answer/answerID` | Edit an answer 
DELETE | `/api/v1/questions/question_id/answer/answerID` | Delete an answer
