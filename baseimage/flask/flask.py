from flask import Flask
from baseimage.config.config import CONFIG


def get_flask_server(name=CONFIG['service_name']):
    """ Returns a sensible default Flask application with a health check built in at /core/health.

    Args:
        name <str>: The name given to the Flask application. Defaults to the service name.
    """
    app = Flask(name)

    @app.route("/core/health")
    def health_check():
        return "{}"

    return app
