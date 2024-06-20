import flask
from registration_page.models import User



def render_cart():
    return flask.render_template(template_name_or_list="cart.html", login=User.query.all())