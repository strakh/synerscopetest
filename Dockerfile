FROM python:3-onbuild

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
