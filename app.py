from flask import Flask
from extensions import db
import os
import sys

app = Flask(__name__)

databse_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# Configure SQLite database
app.config['SECRET_KEY'] ='bad17cf69c4a2799edf13e5e5e64a7b4f4a1cca63ab22ebfee4a346af87190800d1bbd207910d111'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{databse_path}/database/UENote.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 



db.init_app(app=app)


#--routes sections--#

# User
from controller import user_panel
app.add_url_rule('/', view_func=user_panel.main, endpoint='main')
app.add_url_rule('/dashboard', view_func=user_panel.dashboard, endpoint='dashboard')
app.add_url_rule('/projects', view_func=user_panel.projects, endpoint='projects')
app.add_url_rule('/project/create', view_func=user_panel.add_project, endpoint='add_project')
app.add_url_rule('/project/delete/<int:target_id>', view_func=user_panel.delete_project, endpoint='delete_project', methods=['GET' , 'POST'])
app.add_url_rule('/project/edit/<int:project_id>', view_func=user_panel.edit_project, endpoint='edit_project', methods=['POST'])
app.add_url_rule('/project/<int:project_id>/notes', view_func=user_panel.notes, endpoint='notes', methods=['GET' , 'POST'])
app.add_url_rule('/project/<int:project_id>/notes/create', view_func=user_panel.create_note, endpoint='create_notes', methods=['GET' , 'POST'])
app.add_url_rule('/project/<int:project_id>/notes/<int:target_id>/delete', view_func=user_panel.delete_node, endpoint='delete_node', methods=['GET' , 'POST'])
app.add_url_rule('/project/<int:project_id>/notes/<int:note_id>/view', view_func=user_panel.view_note, endpoint='view_note', methods=['GET' , 'POST'])






from models.models import *
@app.before_request
def create_database():
    
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True)
    
