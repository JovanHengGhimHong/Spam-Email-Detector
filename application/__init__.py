import os
from flask import Flask


def create_app():
  app = Flask(
    __name__,
    static_folder='static',
    template_folder='static/templates'
)

  config_path = os.path.join(os.path.dirname(__file__), 'config.cfg')
  app.config.from_pyfile(config_path)

  from .routes import routes
  app.register_blueprint(routes)

  return app


app = create_app()