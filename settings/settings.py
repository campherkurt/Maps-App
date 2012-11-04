# configuration
DATABASE = ''
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

DB_PATH = 'Users/kurtcampher/Projects/personal/maps_django/maps.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % DB_PATH
SQLALCHEMY_MIGRATE_REPO = '/Users/kurtcampher/Projects/personal/maps_django/db_repository'

