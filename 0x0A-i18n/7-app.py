#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    ''' babel config class '''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    ''' get locale from request '''
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in Config.LANGUAGES:
            return locale

    locale = request.headers.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    ''' get timezone '''
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


def get_user():
    ''' returns user from mocked db '''
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None


@app.before_request
def before_request():
    ''' self descriptive '''
    user = get_user()
    g.user = user


@app.route("/", methods=["GET"])
def index():
    """ Returns index """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
