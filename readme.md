# APIs using Flask

---

## Install MongoDB
[MongoDB Installation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

---

## Install Flask

- Create venv
> 1. `mkdir myproject`
> 2. `cd myproject`
> 3. `py -3 -m venv venv`

- Activate Environment:
> 1. `venv\Scripts\activate`

- Installing Flask
> 1. `pip install Flask`

- For Caching:
> 1. `pip install flask_caching`

---

## Installing mongoengine
[MongoEngine](https://docs.mongoengine.org/guide/installing.html)

---

## Populate the data into the mongodb.
- Run the file populate.py
> - `python populate.py`

---

## Use below command to run the flask application
- Here hello.py contains the apis for flask application
> - `flask --app hello --debug run`

---

## Use postman to hit the apis
- http://127.0.0.1:5000/analytics?date=24122022&limit=100&page=1
- http://127.0.0.1:5000/user/search?username=brainyHeron5


This is from HackerEarth MishiPay Contest. This is not the solution. This is for installation and writing apis.

