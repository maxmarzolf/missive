from flask import Blueprint

reminders_bp = Blueprint("reminders_bp", __name__, static_folder="app.static", template_folder="app.templates")

from . import reminders_routes