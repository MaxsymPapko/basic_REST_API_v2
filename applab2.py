from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ініціалізація db та migrate після створення app
    db.init_app(app)
    migrate.init_app(app, db)

    # Тепер імпортуємо blueprint без циклічних імпортів
    from routes.users import users_bp
    from routes.currencies import currencies_bp

    # Реєстрація маршрутів
    app.register_blueprint(users_bp, url_prefix='/api')
    app.register_blueprint(currencies_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return 'Hello, World!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

