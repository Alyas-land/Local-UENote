from flask import render_template, request, url_for, redirect
#from models.models import Project, db
from feature.quries.query import ProjectsQuery

class UserController():

        def main(self):
                return render_template('/main/index.html')
        
        def dashboard(self):
                # Fetch all projects
                projects = ProjectsQuery.fetch_all_projects()
                return render_template('/application_ui/dashboard.html', projects=projects, current_page='dashboard')
        
        def projects(self):
                # Fetch all projects
                projects = ProjectsQuery.fetch_all_projects()
                return render_template('/application_ui/projects.html', projects=projects, current_page='projects')
        

        def add_project(self):
                title = request.args.get('title')
                description = request.args.get('description')
                if (title and description):
                        # Add project to database
                        add_status = ProjectsQuery.add_project(title=title, description=description)
                        if add_status:
                                return redirect('/projects')
                
                        # flash error message
                # flash error message

        def delete_project(self, target_id):
                # Delete project
                del_status = ProjectsQuery.delete_project_by_id(target_id=target_id)
                if del_status:
                        # flash successfull message
                        return redirect('/projects')
                # flash error message
                return redirect('/projects')
        

        def edit_project(self, project_id):
                new_title = request.form['new_title']
                new_description = request.form['new_description']

                edit_status = ProjectsQuery.edit_project_by_id(
                        target_id=project_id,
                        new_title=new_title,
                        new_description=new_description
                )
                if edit_status:
                        # flash success message
                        return redirect('/projects')
                
                 # flash error message


        
