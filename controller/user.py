from flask import render_template, request, url_for, redirect
#from models.models import Project, db
from feature.quries.query import ProjectsQuery, NoteQuery

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

        
        def notes(self, project_id):
                project = ProjectsQuery.fetch_project_by_id(project_id)
                notes = NoteQuery.fetch_all_notes_of_project_by_project_id(project_id)
                return render_template('/application_ui/notes.html', project=project, notes=notes, current_page='notes')
        
        def create_note(self, project_id):
                project = ProjectsQuery.fetch_project_by_id(project_id)
                if request.method == "POST":
                        title = request.form['title']
                        content = request.form['content']
                        create_status = NoteQuery.new_note(
                                title=title,
                                content=content,
                                project_id=project_id
                                )
                        if create_status:
                                # flash success message
                                return redirect(f'/project/{project_id}/notes')
                        # flash error message
                        return redirect(f'/project/{project_id}/notes')

                
                return render_template('/application_ui/create_note.html', project=project)
        
        def delete_node(self, project_id, target_id):
                # Delete project
                del_status = NoteQuery.delete_node_by_id(target_id=target_id)
                if del_status:
                        # flash successfull message
                        return redirect(f'/project/{project_id}/notes')
                # flash error message
                return redirect(f'/project/{project_id}/notes')
        
        def view_note(self, project_id, note_id):
                note = NoteQuery.fetch_note_by_id(note_id=note_id)
                return render_template('/application_ui/view_note.html', note=note)



        
