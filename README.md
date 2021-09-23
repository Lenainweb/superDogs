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
$ python3.9 -m venv env_dog
$ . env_dog/bin/activate 
or
env_dog\Scripts\activate
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