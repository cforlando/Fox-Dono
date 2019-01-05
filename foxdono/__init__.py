"""
Fox Dono is a very special fox here to help with your meetup
"""

from quart import Quart

app = Quart(__name__)
app.config.from_pyfile('config.py')

from . import views
