import flask
import flask_login
from project import login_manager
from registration_page.models import User

def render_authorization_page():
    if flask.request.method == "POST":
        for user in User.query.filter_by(login = flask.request.form['login']):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect('/home_user')
        return flask.redirect('/authorization_next')
    return flask.render_template('auth.html', is_auth = flask_login.current_user.is_authenticated)

def render_authorization_next():
    return flask.render_template(template_name_or_list="auth_register.html")