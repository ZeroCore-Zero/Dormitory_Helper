from flask import Flask
from app import auth
from app.db import db

# Init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BUPT:mysql-bupt-pswd@localhost/BUPT_Helper'
app.register_blueprint(auth.login)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
