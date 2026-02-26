from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys

app = Flask(__name__)

databse_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# Configure SQLite database
app.config['SECRET_KEY'] ='bad17cf69c4a2799edf13e5e5e64a7b4f4a1cca63ab22ebfee4a346af87190800d1bbd207910d111'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{databse_path}/database/UENote.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Create SQLAlchemy instance
db = SQLAlchemy(app)

@app.before_request
def create_database():
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True)
    
