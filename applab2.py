from flask import flask
from routes.users import users_bp
from routes.categories import categories_bp
from routes.records import records_bp

app = flask(__name__)

# Реєструємо "блюпринти" для кожної групи ендпоінтів
app.register_blueprint(users_bp, url_prefix='/api')
'''app.register_blueprint(categories_bp, url_prefix='/api')
app.register_blueprint(records_bp, url_prefix='/api')'''

if __name__ == '__main__':
    app.run(debug=True)
