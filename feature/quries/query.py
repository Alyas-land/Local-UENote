from extensions import db
from models.models import * 

class ProjectsQuery():
    def __init__(self):
        pass

    @staticmethod
    def fetch_all_projects():
        projects = Project.query.all()
        return projects
    
    @staticmethod
    def fetch_project_by_id(target_id):
        target = Project.query.filter_by(id=target_id).one_or_none()
        if target:
            return target
        return None
   
    @staticmethod
    def add_project(title, description):
        new_project = Project(
            title=title,
            description=description
        )
        db.session.add(new_project)
        db.session.commit()
        return True
    
    @staticmethod
    def delete_project_by_id(target_id):
        target = Project.query.filter_by(id=target_id).one_or_none()
        if target:
            db.session.delete(target)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def edit_project_by_id(target_id, new_title, new_description):
        project = Project.query.filter_by(id=target_id).one_or_none()
        if project:
            project.title = new_title
            project.description = new_description
            db.session.commit()
            return True
        return False
    

    
class NoteQuery():
    def __init__(self):
        pass

    @staticmethod
    def fetch_all_notes_of_project_by_project_id(project_id):
        notes = Note.query.filter_by(project_id=project_id).all()
        if notes:
            return notes
        
        return None
    
    @staticmethod
    def fetch_note_by_id(note_id):
        note = Note.query.filter_by(id=note_id).one_or_none()
        if note:
            return note
        return None
    
    @staticmethod
    def new_note(title, content, project_id):
        if title and content:
            new_note = Note(
                title=title,
                content=content,
                project_id=project_id
            )
            db.session.add(new_note)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete_node_by_id(target_id):
        target = Note.query.filter_by(id=target_id).one_or_none()
        if target:
            db.session.delete(target)
            db.session.commit()
            return True
        return False