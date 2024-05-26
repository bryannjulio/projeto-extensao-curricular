from flask import Blueprint, render_template

from . import blueprint
from flask import render_template, request
from jinja2 import TemplateNotFound

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/<template>')
def show_template(template):
    try:
        return render_template(template + '.html')
    except TemplateNotFound:
        return render_template('page-404.html'), 404
