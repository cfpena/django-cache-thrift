# django-cache-thrift
Scholar project using django with redis cache and apache thrift as binary API

## How to run?

#### From source code

Requirements:
- Python 2.7
- virtualEnv

Create a virtual enviroment for python libs

```sh
$ python -m virtualenv env
```

Activate virual env

```sh
$ . ./env/bin/activate
```

Install python requirementes

```sh
$ pip install -r requirements.txt
```

Migrate, Populate database with gifs from tumblr and populate with random views

```sh
$ python manage.py migrate
$ python manage.py populate_db
$ python manage.py populate_views
```

Finally run the thrift server listening on 9090

```sh
$ python manage.py thrift_server
```

### With docker


Install docker
- https://docs.docker.com/install/

Run the container
```sh
$ docker-compose up --build
```
