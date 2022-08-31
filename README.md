# Moove.

This is a mini report version of Moove.


### Requirements for setting up the project.

1. Python3. 
2. Django
3. Virtualenv.
4. Docker.
5. Postgres DB
6. Celery.

### Installation on Mac or linux with Docker

Run the project with Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```
 $ docker-compose up -d
```

Then, the host and the port will be `http://0.0.0.0:8070/`, then use corresponding endpoints in the table 
below :

 #### Endpoints.

| HTTP Method | End Point          | Action              |
|-------------|--------------------|---------------------|
| POST        | api/v1/reports/    | Submit a report     |
| GET         | /api/v1/vehicles/  | Get all Vehicles.   |
| GET         | api/v1/trips/      | Get all trips.      |
| GET         | api/v1/exceptions/ | Get all exceptions. |


**NB :**

For the `api/v1/reports` **POST** endpoint,  the **BODY** is :

```
{
    "email": "any_mail",
    "start_date": "2022-07-14T22:00:00.000Z",
    "end_date": "2022-07-22T22:00:00.000Z"
}
```

### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)
