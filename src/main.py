# Standard imports
import os

# Third party imports
from flask_sqlalchemy import SQLAlchemy

# Custom imports
from src import app

app.config['SECRET_KEY'] = 'asdfqwefqewqev'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootpassword@willyapi_db_1:3306/management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
