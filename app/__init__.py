import os
import json
import datetime

import flask
from flask import session, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from config import Config


class Blog(flask.Flask):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config: type = Config) -> Blog:
    app = Blog(
        __name__,
        static_folder="public"
    )
    app.config.from_object(config)
    print(config.IS_PRODUCTION)

    load_modules(app)
    define_blueprints(app)
    
    return app

def load_modules(app: flask.Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)


def define_blueprints(app: flask.Flask):
    from app.routes import(
        main,
        blog,
        auth
    )

    # Vite assets blueprints
    assets_blueprint = flask.Blueprint(
        "assets",
        __name__,
        static_folder="build/assets/bundled",
        static_url_path="/assets/bundled"
    )
    manifest = {}
    if app.config['IS_PRODUCTION']:
        manifest_path = os.path.join(app.config["APPLICATION_ROOT"], "build/assets/manifest.json")
        try:
            with open(manifest_path, "r") as content:
                manifest = json.load(content)
        except OSError as exception:
            raise OSError(
                f"Manifest file not found. Run 'npm run build'."
            ) from exception

    @assets_blueprint.app_context_processor
    def add_context():
        def dev_asset(file_path: str):
            return f"{app.config['VITE_ORIGIN']}/assets/{file_path}"
        
        def prod_asset(file_path: str):
            try:
                return f"/assets/{manifest[file_path]['file']}"
            except:
                return "asset-not-found"
            
        return {
            "asset": prod_asset if app.config["IS_PRODUCTION"] else dev_asset,
            "is_production": app.config["IS_PRODUCTION"]
        }

    app.register_blueprint(assets_blueprint)
    app.register_blueprint(main.bp)
    app.register_blueprint(blog.bp, url_prefix="/blog")
    app.register_blueprint(auth.bp, url_prefix="/auth")

# def configure_hook(app: flask.Flask):
#     @app.before_request
#     def before_request():
#         session.permanent = True
#         app.permanent_session_lifetime = datetime.timedelta(minutes=20)
#         session.modified = True
#         g.user = current_user