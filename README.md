# lovemint.assignment

Lovemint Assignment Django Backend


## Run Locally

Clone the project

```bash
  git clone https://github.com/rkisdp/lovemint.assignment
```

Go to the project directory

```bash
  cd lovemint.assignment
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  # if want to use docker
  docker-compose up

  # if want to run django
  # to initial django local server
  python manage.py runserver
  
  # to initial celery
  celery -A lovemint_django_backend.celery worker -l info

```APIs(on docker)
  url: 0.0.0.0:8000/account/register_user/
  request: POST
  body(form-data): mandatory: name, age, gender
                   optional: image, description_text, location, timestamp

  url: 0.0.0.0:8000/account/list_users/
  request: GET
  query_params: page, page_size

  url: 0.0.0.0:8000/account/resize_user_image/<user_id>/
  request: GET

```
