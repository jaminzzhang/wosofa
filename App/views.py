from App import app
from flask import Blueprint, render_template, flash, redirect, url_for, session, request, g
from jinja2 import TemplateNotFound
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/film/<film_id>')
def filmInfo(film_id):
    return "Film:%s" % film_id