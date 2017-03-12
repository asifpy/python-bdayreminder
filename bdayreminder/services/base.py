from jinja2 import Environment, FileSystemLoader

from bdayreminder.helpers import get_parser
from bdayreminder.settings import TEMPLATE_DIRS


class BaseReminder(object):
    def __init__(self, bday_guy, *args, **kwargs):
        self.username = get_parser(self.provider, 'username')
        self.password = get_parser(self.provider, 'password')
        self.env = self.jinja_env()
        self.bday_guy = bday_guy

    def __call__(self):
        self.execute()

    def jinja_env(self):
        loader = FileSystemLoader(TEMPLATE_DIRS)
        return Environment(loader=loader)
