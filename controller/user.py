from flask import render_template, request, url_for, redirect
from models.models import Project, db

class UserController():

        def main(self):
                return render_template('/main/index.html')
        
        def dashboard(self):
                # Fetch all projects
                projects = Project.query.all()

                return render_template('/application_ui/dashboard.html', projects=projects)
        

        def add_project(self):
            title = request.args.get('title')
            description = request.args.get('description')

            if (title and description):
                project = Project(
                    title = title,
                    description = description
                    )
                db.session.add(project)
                db.session.commit()
            
                return redirect('/dashboard')
        
