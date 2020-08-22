from flask import Flask
from flask import render_template

app = Flask(__name__)

from app import public
from app import admin