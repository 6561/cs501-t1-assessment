web: gunicorn project.server.wsgi:app
heroku ps:scale web=1
release: export FLASK_APP=project.server && export APP_SETTINGS="project.server.config.ProductionConfig" && flask db init && flask db migrate && flask db upgrade

