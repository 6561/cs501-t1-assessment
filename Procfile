web: gunicorn project.server.wsgi:app
heroku ps:scale web=1
release: ./tables.sh

