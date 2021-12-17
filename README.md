# E-learning platform
University group project. Web application where you can share and access learning materials, do quizes and more!

## Table of contents
* [Demo](#demo)
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## Demo
You can find working demo at link (#tbd)

## General info
[Requirements and documentation](https://docs.google.com/document/d/1ePbhBakCs22f5DQX22LmuklZ90XHLyQWQnNu46i2yyA/edit?usp=sharing)


## Technologies
Project is created with:
* Django
* Angular
* Clarity UI library
	
## Setup
### Frontend setup
To set up local frontend development environment you need installed [NodeJS with npm](https://nodejs.org/en/download/) and (Angular CLI)[https://angular.io/cli].
* Go to the frontend folder `cd elearning-frontend`
* Install project dependencies `npm install`
* Start project `npm start`
* Go to http://localhost:4200/
### Backend setup
To setup local backend development enviornment you nedd intalled Python 3 and Django
* Go to the backend folder `cd elearnig`
* Make migrations `python3 manage.py makemigrations`
* Run migrations `python3 manage.py migrate`
* Run server `python3 manage.py runserver`
* API will be available at http://localhost:8000/
