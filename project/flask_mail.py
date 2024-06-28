import flask_mail
from .settings import project

project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USERNAME"] = "artutkakish5@gmail.com"
project.config["MAIL_PASSWORD"] = "btak jskx qwkf nywr"

mail = flask_mail.Mail(project)