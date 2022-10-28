## CatsShop
A simple web application that displays cats, sorts them by age and name. It stores and serves data using a Flask web application.

### Start the app in Docker

>Download the code
```
$ git clone https://github.com/spacefellow/CatsShop.git
Create .dbenv and .flaskenv files in root folder
$ cd CatsShop
```

>.flaskenv contains
```
FLASK_APP='./app/run.py'
FLASK_ENV=development
DATABASE_URL=your db url
SECRET_KEY=your secret key
```

>.dbenv contains
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=name of database
```

>Start the APP in Docker
```
$ docker-compose up --build 
```
At this point, the app runs at http://localhost:8000/


### Set Up the app in Windows

>Download the code
```
$ git clone https://github.com/spacefellow/CatsShop.git
Create .flaskenv file in root folder
$ cd CatsShop
```

>Install modules VENV
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```
>Set Up Flask Environment
```
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
```

>Start the app
```
$ flask run
```
At this point, the app runs at http://127.0.0.1:5000/

### Learn More
To learn Flask, check out the [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/).
