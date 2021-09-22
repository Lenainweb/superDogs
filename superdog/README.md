## Dependencies
* Django

## Setting up

##### Clone the repo

```
$ git clone https://github.com/Lenainweb/superDogs.git
$ cd superdog
```

##### Initialize a virtualenv

```
$ python3.9 -m venv venv
$ . venv/bin/activate
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Create the database

```
$ python manage.py migrate
```

## Running the server

```
$ python manage.py runserver