# Standard imports
import os

# Third party imports
from flask_sqlalchemy import SQLAlchemy

# Custom imports
from src import app

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
