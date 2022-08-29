# Moove.

This is a mini report version of Moove.


### Requirements for setting up the project.
1. Python3. 
2. Django
3. Virtualenv.
4. Docker.
5. Postgres DB

### Installation on Mac

1 . First clone this repository 

```
$ git clone https://github.com/huxaiphaer/moove.gitt
```

2 . Add the following variables in your Environment Variables permanently:

```
DATABASE_URL=postgres://captiq:password@localhost:5432/moove_db
DEBUG=False
SECRET_KEY=SECRET_KEY
EMAIL_HOST_USER=sample@gmail.com
DEFAULT_FROM_EMAIL=sample@gmail.com
EMAIL_HOST_PASSWORD=sample
BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379

```

After, setting up the environment variables add create a Postgres Database called `moove_db`,
followed by running migrations with the commands below to create all the necessary tables


3 . Then, create a virtual environment and install in on Mac :

```
$ virtualenv env
$ source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```
$ pip3 install -r requirements.txt
```

**NOTE :**
- The commands below won't run unless  you have your Redis server running and as well
as setting all the environment variables above.

```
$ ./manage.py migrate
$ ./manage.py run_data_exceptions
$ ./manage.py run_data_trips  
$ ./manage.py run_data_vehicles 

```

What happens for the commands below :

`run_data_trips` - (Populates data for Trips)

`run_data_vehicles` - (Populates data for vehicles)

`run_data_exceptions` - (Populates data for exceptions)

`clear_all_tables`  - (Clear all tables)


## Running with Docker.

The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```python3

 $ docker-compose up --build

```


 #### Endpoints.

| HTTP Method | End Point          | Action              |
|-------------|--------------------|---------------------|
| POST        | api/v1/reports/    | Submit a report     |
| GET         | /api/v1/vehicles/  | Get all Vehicles.   |
| GET         | api/v1/trips/      | Get all trips.      |
| GET         | api/v1/exceptions/ | Get all exceptions. |



### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)