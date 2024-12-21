import os
from flask import Flask
from routes.users import users_bp
from routes.categories import categories_bp
from routes.records import records_bp

app = Flask(__name__)

# Реєструємо "блюпринти" для кожної групи ендпоінтів
app.register_blueprint(users_bp, url_prefix='/api')
'''app.register_blueprint(categories_bp, url_prefix='/api')
app.register_blueprint(records_bp, url_prefix='/api')'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)