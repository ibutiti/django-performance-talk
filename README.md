# Django Performance Optimization 101

Devish Talk

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

1. Run database migrations.

```
python manage.py migrate
```

1. Start the dev server

```
python manage.py runserver
```

Your project should be running and accessible on `localhost:8000`
