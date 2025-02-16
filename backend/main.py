from flask import Flask
from tomllib import load
from app import auth
from app.db import db

with open("./config.toml", "rb") as file:
    config = load(file)

# Init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config['mysql']['username']}:{config['mysql']['password']}@{config['mysql']['address']}/{config['mysql']['database']}"
app.register_blueprint(auth.login)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
