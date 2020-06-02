from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object("config.ConfigDev")

    with app.app_context():

        from . import reminders
        app.register_blueprint(reminders.reminders_bp)

        return app