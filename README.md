### How to run the project locally

##### Install required packages
```
$ pip install -r requirements/dev.txt
```

##### Create the database and the user
For the dev environment the db, username and password default to the project name

##### Run migrations
```
$ python src/manage.py migrate
``` 
You can also make `src/manage.py` executable and run it without `python`
```
$ chmod +x src/manage.py
$ src/manage.py migrate
``` 

##### Install front-end dependencies and run dev build task
```
$ npm install
$ npm run dev
```

##### Start the dev server
```
$ (python) src/manage.py runserver 
```