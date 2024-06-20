import flask, flask_sqlalchemy
import flask_sqlalchemy.query
from project.settings import db
from registration_page.models import User
# from registration_page.views import username

def render_home():
    return flask.render_template(template_name_or_list='home.html')



def render_home_user():
    return flask.render_template(template_name_or_list='home_user_page.html', login=User.query.all())