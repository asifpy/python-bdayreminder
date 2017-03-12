import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REMINDER_DIR = os.path.join(BASE_DIR, 'bdayreminder')

# database file for sqlite3
DATABASE = 'bdayreminder.db'

# temaplte directory which will used by jinja2 to load notification messages
TEMPLATE_DIRS = os.path.join(REMINDER_DIR, 'templates')

# configuration file for gmail, way2sms credentials
CONFIG_FILE = os.path.join(REMINDER_DIR, 'config.ini')
