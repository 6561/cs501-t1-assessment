import os
import sys

if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(
        branch=True,
        include='project/*',
        omit=[
            'project/tests/*',
            'project/server/config.py',
            'project/server/*/__init__.py'
        ]
    )
    COV.start()

import click
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import create_engine

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.ProductionConfig'
)
app.config.from_object(app_settings)

engine = create_engine('postgres://sgbuguiryacoda:a869c2eb1ff0fa6c5a118a5d95b70a6faa9db86d0e649dca0f1a905b69ca5b95@ec2-44-198-100-81.compute-1.amazonaws.com:5432/d8fphn9gmdhv7n')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.models import User
migrate = Migrate(app, db)

@app.route("/")
def root_site():
    return "<p>It works! Welcome!</p>"

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
                help='Run tests under code coverage.')
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        if COV:
            COV.stop()
            COV.save()
            print('Coverage Summary:')
            COV.report()
            basedir = os.path.abspath(os.path.dirname(__file__))
            covdir = os.path.join(basedir, 'tmp/coverage')
            COV.html_report(directory=covdir)
            print('HTML version: file://%s/index.html' % covdir)
            COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')