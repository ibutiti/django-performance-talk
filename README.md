# Django Performance Optimization 101

A Developerish workshop I gave on Wednesday, May 11th, 2022.

The session recording is available on [YouTube](https://youtu.be/paNYY6eHxao).

Accompanying slides in PDF are on the root of this repository.

## Tools I Mention
- [Django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [Django Silk](https://silk.readthedocs.io/)
- [Django Rq (redis queues)](https://github.com/rq/django-rq)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Rabbitmq](https://www.rabbitmq.com/)

## Project Setup

### Prerequisites

You'll need these already setup to run this project:

- Python `3.8` to `3.10` (I'm using 3.10.4)

### Installation

1. Clone this repo and `cd` into the project root

1. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run database migrations.

```
python manage.py migrate
```

5. Seed the database
```
python manage.py seed_db
```
6. Start the dev server

```
python manage.py runserver
```

Your project should be running and accessible on `localhost:8000`

## API Documentation
OpenAPI documentation is available on `schema.yml` at the root of this repository or when the project is running on `http://localhost:8000/api/schema/swagger-ui/`
