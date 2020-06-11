from flask import Blueprint
from . import sms_routes

sms_bp = Blueprint("sms_bp", __name__, static_folder="app.static", template_folder="app.templates")


